from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List
import os
import uuid

from app.database.db import get_db
from app.models.genealogy import (
    Genealogy, GenealogyStatus, GenealogyMember, 
    GenealogyDocument, GenealogyUserPermission, GenealogyPermission
)
from app.api.schemas.genealogy import (
    GenealogyCreate, GenealogyUpdate, GenealogyResponse,
    GenealogyMemberCreate, GenealogyMemberResponse,
    GenealogyDocumentCreate, GenealogyDocumentResponse,
    GenealogyPermissionUpdate
)
from app.api.controllers.auth import get_current_active_user
from app.models.user import User

router = APIRouter(prefix="/genealogy", tags=["族谱管理"])


@router.post("/create", response_model=GenealogyResponse)
def create_genealogy(
    genealogy: GenealogyCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """创建族谱"""
    new_genealogy = Genealogy(
        name=genealogy.name,
        clan_id=genealogy.clan_id,
        creator_id=current_user.id,
        description=genealogy.description,
        status=GenealogyStatus.DRAFT
    )
    
    db.add(new_genealogy)
    db.commit()
    db.refresh(new_genealogy)
    
    # 为创建者添加所有权限
    permissions = [
        GenealogyPermission.VIEW,
        GenealogyPermission.EDIT,
        GenealogyPermission.DOWNLOAD
    ]
    
    for permission in permissions:
        perm = GenealogyUserPermission(
            genealogy_id=new_genealogy.id,
            user_id=current_user.id,
            permission=permission
        )
        db.add(perm)
    
    db.commit()
    
    return new_genealogy


@router.get("/my", response_model=List[GenealogyResponse])
def get_my_genealogies(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """获取我的族谱列表"""
    # 获取创建的族谱
    created_genealogies = db.query(Genealogy).filter(
        Genealogy.creator_id == current_user.id
    ).all()
    
    # 获取有权限的族谱
    permitted_genealogies = db.query(Genealogy).join(
        GenealogyUserPermission
    ).filter(
        GenealogyUserPermission.user_id == current_user.id
    ).all()
    
    # 合并去重
    genealogy_ids = set()
    result = []
    
    for genealogy in created_genealogies + permitted_genealogies:
        if genealogy.id not in genealogy_ids:
            genealogy_ids.add(genealogy.id)
            result.append(genealogy)
    
    return result


@router.get("/{genealogy_id}", response_model=GenealogyResponse)
def get_genealogy_detail(
    genealogy_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """获取族谱详情"""
    genealogy = db.query(Genealogy).filter(
        Genealogy.id == genealogy_id
    ).first()
    
    if not genealogy:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="族谱不存在"
        )
    
    # 检查权限
    has_permission = db.query(GenealogyUserPermission).filter(
        GenealogyUserPermission.genealogy_id == genealogy_id,
        GenealogyUserPermission.user_id == current_user.id
    ).first()
    
    if not has_permission and genealogy.creator_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权限访问"
        )
    
    return genealogy


@router.put("/{genealogy_id}", response_model=GenealogyResponse)
def update_genealogy(
    genealogy_id: str,
    genealogy: GenealogyUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """更新族谱"""
    existing_genealogy = db.query(Genealogy).filter(
        Genealogy.id == genealogy_id
    ).first()
    
    if not existing_genealogy:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="族谱不存在"
        )
    
    if existing_genealogy.creator_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权限修改"
        )
    
    update_data = genealogy.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(existing_genealogy, field, value)
    
    db.commit()
    db.refresh(existing_genealogy)
    
    return existing_genealogy


@router.delete("/{genealogy_id}")
def delete_genealogy(
    genealogy_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """删除族谱"""
    genealogy = db.query(Genealogy).filter(
        Genealogy.id == genealogy_id
    ).first()
    
    if not genealogy:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="族谱不存在"
        )
    
    if genealogy.creator_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权限删除"
        )
    
    db.delete(genealogy)
    db.commit()
    
    return {"message": "删除成功"}


@router.post("/{genealogy_id}/members", response_model=GenealogyMemberResponse)
def add_member(
    genealogy_id: str,
    member: GenealogyMemberCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """添加族员"""
    # 检查权限
    genealogy = db.query(Genealogy).filter(
        Genealogy.id == genealogy_id
    ).first()
    
    if not genealogy:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="族谱不存在"
        )
    
    has_edit_permission = db.query(GenealogyUserPermission).filter(
        GenealogyUserPermission.genealogy_id == genealogy_id,
        GenealogyUserPermission.user_id == current_user.id,
        GenealogyUserPermission.permission == GenealogyPermission.EDIT
    ).first()
    
    if not has_edit_permission and genealogy.creator_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权限编辑"
        )
    
    new_member = GenealogyMember(
        genealogy_id=genealogy_id,
        name=member.name,
        gender=member.gender,
        birth_date=member.birth_date,
        death_date=member.death_date,
        father_id=member.father_id,
        mother_id=member.mother_id,
        spouse_id=member.spouse_id,
        generation=member.generation,
        description=member.description
    )
    
    db.add(new_member)
    
    # 更新成员数量
    genealogy.member_count += 1
    
    db.commit()
    db.refresh(new_member)
    
    return new_member


@router.post("/{genealogy_id}/documents", response_model=GenealogyDocumentResponse)
async def upload_document(
    genealogy_id: str,
    file: UploadFile = File(...),
    name: str = Form(...),
    description: str = Form(None),
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """上传家族文献"""
    # 检查权限
    genealogy = db.query(Genealogy).filter(
        Genealogy.id == genealogy_id
    ).first()
    
    if not genealogy:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="族谱不存在"
        )
    
    has_edit_permission = db.query(GenealogyUserPermission).filter(
        GenealogyUserPermission.genealogy_id == genealogy_id,
        GenealogyUserPermission.user_id == current_user.id,
        GenealogyUserPermission.permission == GenealogyPermission.EDIT
    ).first()
    
    if not has_edit_permission and genealogy.creator_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权限上传"
        )
    
    # 保存文件
    file_extension = os.path.splitext(file.filename)[1]
    file_name = f"{uuid.uuid4()}{file_extension}"
    file_path = f"documents/{genealogy_id}/{file_name}"
    
    # 确保目录存在
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    
    # 创建文档记录
    new_document = GenealogyDocument(
        genealogy_id=genealogy_id,
        name=name,
        file_path=file_path,
        file_type=file.content_type,
        size=len(content),
        description=description,
        uploaded_by=current_user.id
    )
    
    db.add(new_document)
    db.commit()
    db.refresh(new_document)
    
    return new_document


@router.put("/{genealogy_id}/permissions")
def set_permissions(
    genealogy_id: str,
    permission: GenealogyPermissionUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """设置族谱权限"""
    genealogy = db.query(Genealogy).filter(
        Genealogy.id == genealogy_id
    ).first()
    
    if not genealogy:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="族谱不存在"
        )
    
    if genealogy.creator_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权限设置权限"
        )
    
    # 检查用户是否存在
    user = db.query(User).filter(
        User.id == permission.user_id
    ).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在"
        )
    
    # 检查是否已有权限
    existing_permission = db.query(GenealogyUserPermission).filter(
        GenealogyUserPermission.genealogy_id == genealogy_id,
        GenealogyUserPermission.user_id == permission.user_id,
        GenealogyUserPermission.permission == permission.permission
    ).first()
    
    if existing_permission:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="权限已存在"
        )
    
    new_permission = GenealogyUserPermission(
        genealogy_id=genealogy_id,
        user_id=permission.user_id,
        permission=permission.permission
    )
    
    db.add(new_permission)
    db.commit()
    
    return {"message": "权限设置成功"}
