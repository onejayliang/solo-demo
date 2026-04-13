from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database.db import get_db
from app.models.interaction import CultureShare
from app.api.schemas.interaction import (
    CultureShareCreate, CultureShareResponse
)
from app.api.controllers.auth import get_current_active_user
from app.models.user import User

router = APIRouter(prefix="/culture", tags=["文化分享"])


@router.post("/share", response_model=CultureShareResponse)
def share_culture(
    culture: CultureShareCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """分享家风"""
    new_culture = CultureShare(
        user_id=current_user.id,
        clan_id=culture.clan_id,
        title=culture.title,
        content=culture.content
    )
    
    db.add(new_culture)
    db.commit()
    db.refresh(new_culture)
    
    return new_culture


@router.get("/list", response_model=List[CultureShareResponse])
def get_cultures(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """获取家风列表"""
    cultures = db.query(CultureShare).order_by(
        CultureShare.created_at.desc()
    ).all()
    
    return cultures


@router.get("/{culture_id}", response_model=CultureShareResponse)
def get_culture_detail(
    culture_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """获取家风详情"""
    culture = db.query(CultureShare).filter(
        CultureShare.id == culture_id
    ).first()
    
    if not culture:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="分享不存在"
        )
    
    return culture


@router.post("/{culture_id}/like")
def like_culture(
    culture_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """点赞家风"""
    culture = db.query(CultureShare).filter(
        CultureShare.id == culture_id
    ).first()
    
    if not culture:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="分享不存在"
        )
    
    # 这里可以添加点赞逻辑，比如记录用户点赞
    # 简单实现：直接增加点赞数
    culture.likes_count += 1
    db.commit()
    
    return {"message": "点赞成功", "likes_count": culture.likes_count}
