from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.database.db import get_db
from app.models.interaction import Activity, ActivityParticipant
from app.api.schemas.interaction import (
    ActivityCreate, ActivityResponse
)
from app.api.controllers.auth import get_current_active_user
from app.models.user import User

router = APIRouter(prefix="/activity", tags=["活动管理"])


@router.post("/create", response_model=ActivityResponse)
def create_activity(
    activity: ActivityCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """创建活动"""
    new_activity = Activity(
        name=activity.name,
        clan_id=activity.clan_id,
        organizer_id=current_user.id,
        description=activity.description,
        start_time=activity.start_time,
        end_time=activity.end_time,
        location=activity.location,
        max_participants=activity.max_participants,
        status="upcoming"
    )
    
    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)
    
    return new_activity


@router.get("/list", response_model=List[ActivityResponse])
def get_activities(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """获取活动列表"""
    activities = db.query(Activity).order_by(
        Activity.created_at.desc()
    ).all()
    
    return activities


@router.get("/{activity_id}", response_model=ActivityResponse)
def get_activity_detail(
    activity_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """获取活动详情"""
    activity = db.query(Activity).filter(
        Activity.id == activity_id
    ).first()
    
    if not activity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="活动不存在"
        )
    
    return activity


@router.post("/{activity_id}/join")
def join_activity(
    activity_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """报名活动"""
    activity = db.query(Activity).filter(
        Activity.id == activity_id
    ).first()
    
    if not activity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="活动不存在"
        )
    
    # 检查是否已经报名
    existing_participant = db.query(ActivityParticipant).filter(
        ActivityParticipant.activity_id == activity_id,
        ActivityParticipant.user_id == current_user.id
    ).first()
    
    if existing_participant:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="已经报名该活动"
        )
    
    # 检查人数限制
    if activity.max_participants and activity.participant_count >= activity.max_participants:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="活动人数已满"
        )
    
    # 创建参与者记录
    participant = ActivityParticipant(
        activity_id=activity_id,
        user_id=current_user.id,
        status="registered"
    )
    
    db.add(participant)
    
    # 更新活动参与人数
    activity.participant_count += 1
    
    db.commit()
    
    return {"message": "报名成功"}


@router.get("/{activity_id}/participants")
def get_activity_participants(
    activity_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """获取活动参与者列表"""
    activity = db.query(Activity).filter(
        Activity.id == activity_id
    ).first()
    
    if not activity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="活动不存在"
        )
    
    participants = db.query(ActivityParticipant).filter(
        ActivityParticipant.activity_id == activity_id
    ).all()
    
    return participants
