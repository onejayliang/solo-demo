from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Integer, Boolean
from sqlalchemy.sql import func
from app.database.db import SQLAlchemyBase
import uuid


class ChatRoom(SQLAlchemyBase):
    """聊天室模型"""
    __tablename__ = "chat_rooms"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(200), nullable=False)
    clan_id = Column(String, ForeignKey("clans.id"), nullable=True, index=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    def __repr__(self):
        return f"<ChatRoom {self.name}>"


class Message(SQLAlchemyBase):
    """消息模型"""
    __tablename__ = "messages"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    chat_room_id = Column(String, ForeignKey("chat_rooms.id"), nullable=False, index=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False, index=True)
    content = Column(Text, nullable=False)
    message_type = Column(String(50), default="text", nullable=False)  # text, image, file
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    def __repr__(self):
        return f"<Message {self.id}>"


class Activity(SQLAlchemyBase):
    """活动模型"""
    __tablename__ = "activities"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(200), nullable=False, index=True)
    clan_id = Column(String, ForeignKey("clans.id"), nullable=True, index=True)
    organizer_id = Column(String, ForeignKey("users.id"), nullable=False)
    description = Column(Text, nullable=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=True)
    location = Column(String(500), nullable=False)
    max_participants = Column(Integer, nullable=True)
    participant_count = Column(Integer, default=0, nullable=False)
    status = Column(String(50), default="upcoming", nullable=False)  # upcoming, ongoing, completed, cancelled
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    def __repr__(self):
        return f"<Activity {self.name}>"


class ActivityParticipant(SQLAlchemyBase):
    """活动参与者模型"""
    __tablename__ = "activity_participants"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    activity_id = Column(String, ForeignKey("activities.id"), nullable=False, index=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False, index=True)
    status = Column(String(50), default="registered", nullable=False)  # registered, attended, cancelled
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    def __repr__(self):
        return f"<ActivityParticipant {self.id}>"


class CultureShare(SQLAlchemyBase):
    """家风分享模型"""
    __tablename__ = "culture_shares"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False, index=True)
    clan_id = Column(String, ForeignKey("clans.id"), nullable=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    content = Column(Text, nullable=False)
    likes_count = Column(Integer, default=0, nullable=False)
    comments_count = Column(Integer, default=0, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    def __repr__(self):
        return f"<CultureShare {self.title}>"


class ZongQinCard(SQLAlchemyBase):
    """宗亲名片模型"""
    __tablename__ = "zongqin_cards"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), unique=True, nullable=False, index=True)
    clan_id = Column(String, ForeignKey("clans.id"), nullable=True, index=True)
    generation = Column(String(50), nullable=True)
    style_name = Column(String(100), nullable=True)
    introduction = Column(Text, nullable=True)
    qr_code = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    def __repr__(self):
        return f"<ZongQinCard {self.user_id}>"
