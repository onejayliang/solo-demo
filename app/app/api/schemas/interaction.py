from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class ChatRoomResponse(BaseModel):
    """聊天室响应"""
    id: str
    name: str
    clan_id: Optional[str]
    description: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class MessageCreate(BaseModel):
    """发送消息"""
    content: str = Field(..., min_length=1, description="消息内容")
    message_type: Optional[str] = Field("text", description="消息类型")


class MessageResponse(BaseModel):
    """消息响应"""
    id: str
    chat_room_id: str
    user_id: str
    content: str
    message_type: str
    created_at: datetime

    class Config:
        from_attributes = True


class ActivityCreate(BaseModel):
    """创建活动"""
    name: str = Field(..., min_length=1, max_length=200, description="活动名称")
    clan_id: Optional[str] = Field(None, description="宗族ID")
    description: Optional[str] = Field(None, description="活动描述")
    start_time: datetime = Field(..., description="开始时间")
    end_time: Optional[datetime] = Field(None, description="结束时间")
    location: str = Field(..., min_length=1, max_length=500, description="活动地点")
    max_participants: Optional[int] = Field(None, description="最大参与人数")


class ActivityResponse(BaseModel):
    """活动响应"""
    id: str
    name: str
    clan_id: Optional[str]
    organizer_id: str
    description: Optional[str]
    start_time: datetime
    end_time: Optional[datetime]
    location: str
    max_participants: Optional[int]
    participant_count: int
    status: str
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class CultureShareCreate(BaseModel):
    """分享家风"""
    title: str = Field(..., min_length=1, max_length=200, description="标题")
    clan_id: Optional[str] = Field(None, description="宗族ID")
    content: str = Field(..., min_length=1, description="内容")


class CultureShareResponse(BaseModel):
    """家风分享响应"""
    id: str
    user_id: str
    clan_id: Optional[str]
    title: str
    content: str
    likes_count: int
    comments_count: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class ZongQinCardResponse(BaseModel):
    """宗亲名片响应"""
    id: str
    user_id: str
    clan_id: Optional[str]
    generation: Optional[str]
    style_name: Optional[str]
    introduction: Optional[str]
    qr_code: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
