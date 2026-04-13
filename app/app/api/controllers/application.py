from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.database.db import get_db
from app.models.ancestor_data import Application, ApplicationStatus, AncestorData, Clan
from app.api.schemas.ancestor_data import (
    ApplicationCreate, ApplicationReview, ApplicationResponse
)
from app.api.controllers.auth import get_current_active_user
from app.models.user import User

router = APIRouter(prefix="/application", tags=["认祖申请"])


@router.post("/submit", response_model=ApplicationResponse)
def submit_application(
    application: ApplicationCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """提交认祖申请"""
    # 验证祖上资料
    ancestor_data = db.query(AncestorData).filter(
        AncestorData.id == application.ancestor_data_id
    ).first()
    
    if not ancestor_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="祖上资料不存在"
        )
    
    if ancestor_data.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权限使用此资料"
        )
    
    # 验证宗族
    clan = db.query(Clan).filter(
        Clan.id == application.clan_id
    ).first()
    
    if not clan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="宗族不存在"
        )
    
    # 检查是否已有申请
    existing_application = db.query(Application).filter(
        Application.user_id == current_user.id,
        Application.clan_id == application.clan_id,
        Application.status == ApplicationStatus.PENDING
    ).first()
    
    if existing_application:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="已有未处理的申请"
        )
    
    # 创建申请
    new_application = Application(
        user_id=current_user.id,
        ancestor_data_id=application.ancestor_data_id,
        clan_id=application.clan_id,
        reason=application.reason,
        status=ApplicationStatus.PENDING
    )
    
    db.add(new_application)
    db.commit()
    db.refresh(new_application)
    
    return new_application


@router.get("/my", response_model=List[ApplicationResponse])
def get_my_applications(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """获取我的申请列表"""
    applications = db.query(Application).filter(
        Application.user_id == current_user.id
    ).order_by(Application.created_at.desc()).all()
    
    return applications


@router.get("/{application_id}", response_model=ApplicationResponse)
def get_application_detail(
    application_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """获取申请详情"""
    application = db.query(Application).filter(
        Application.id == application_id
    ).first()
    
    if not application:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="申请不存在"
        )
    
    if application.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权限访问"
        )
    
    return application


@router.put("/{application_id}/review")
def review_application(
    application_id: str,
    review: ApplicationReview,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """审核认祖申请"""
    # 检查用户是否为管理员
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权限审核"
        )
    
    application = db.query(Application).filter(
        Application.id == application_id
    ).first()
    
    if not application:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="申请不存在"
        )
    
    if application.status != ApplicationStatus.PENDING:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="申请已处理"
        )
    
    # 更新申请状态
    application.status = review.status
    application.review_notes = review.review_notes
    application.reviewed_by = current_user.id
    application.reviewed_at = datetime.utcnow()
    
    # 如果审核通过，可以在这里添加用户到宗族的逻辑
    
    db.commit()
    db.refresh(application)
    
    return {
        "message": "审核成功",
        "status": application.status
    }


@router.get("/admin/pending", response_model=List[ApplicationResponse])
def get_pending_applications(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """获取待审核的申请（管理员）"""
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权限访问"
        )
    
    applications = db.query(Application).filter(
        Application.status == ApplicationStatus.PENDING
    ).order_by(Application.created_at.asc()).all()
    
    return applications
