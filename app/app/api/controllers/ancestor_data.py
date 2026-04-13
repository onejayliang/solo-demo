from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database.db import get_db
from app.models.ancestor_data import AncestorData, AncestorDataStatus
from app.api.schemas.ancestor_data import (
    AncestorDataCreate, AncestorDataUpdate, AncestorDataResponse
)
from app.api.controllers.auth import get_current_active_user
from app.models.user import User

router = APIRouter(prefix="/ancestor-data", tags=["祖上资料"])


@router.post("/submit", response_model=AncestorDataResponse)
def submit_data(
    data: AncestorDataCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """提交祖上资料"""
    ancestor_data = AncestorData(
        user_id=current_user.id,
        surname=data.surname,
        hall_name=data.hall_name,
        ancestor_name=data.ancestor_name,
        origin=data.origin,
        description=data.description,
        status=AncestorDataStatus.PENDING
    )
    
    db.add(ancestor_data)
    db.commit()
    db.refresh(ancestor_data)
    
    return ancestor_data


@router.get("/my", response_model=List[AncestorDataResponse])
def get_my_data(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """获取我的祖上资料列表"""
    data_list = db.query(AncestorData).filter(
        AncestorData.user_id == current_user.id
    ).order_by(AncestorData.created_at.desc()).all()
    
    return data_list


@router.get("/{data_id}", response_model=AncestorDataResponse)
def get_data_detail(
    data_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """获取祖上资料详情"""
    data = db.query(AncestorData).filter(
        AncestorData.id == data_id
    ).first()
    
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="资料不存在"
        )
    
    if data.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权限访问"
        )
    
    return data


@router.put("/{data_id}", response_model=AncestorDataResponse)
def update_data(
    data_id: str,
    data: AncestorDataUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """更新祖上资料"""
    ancestor_data = db.query(AncestorData).filter(
        AncestorData.id == data_id
    ).first()
    
    if not ancestor_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="资料不存在"
        )
    
    if ancestor_data.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权限修改"
        )
    
    if ancestor_data.status != AncestorDataStatus.PENDING:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="资料已处理，无法修改"
        )
    
    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(ancestor_data, field, value)
    
    db.commit()
    db.refresh(ancestor_data)
    
    return ancestor_data


@router.delete("/{data_id}")
def delete_data(
    data_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """删除祖上资料"""
    ancestor_data = db.query(AncestorData).filter(
        AncestorData.id == data_id
    ).first()
    
    if not ancestor_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="资料不存在"
        )
    
    if ancestor_data.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权限删除"
        )
    
    db.delete(ancestor_data)
    db.commit()
    
    return {"message": "删除成功"}
