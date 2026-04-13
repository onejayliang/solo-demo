from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Enum, Boolean
from sqlalchemy.sql import func
from app.database.db import SQLAlchemyBase
import uuid
import enum


class AncestorDataStatus(str, enum.Enum):
    """祖上资料状态"""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class ApplicationStatus(str, enum.Enum):
    """认祖申请状态"""
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class Clan(SQLAlchemyBase):
    """宗族模型"""
    __tablename__ = "clans"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(100), nullable=False, index=True)
    surname = Column(String(20), nullable=False, index=True)
    hall_name = Column(String(100), nullable=True, index=True)
    origin = Column(String(200), nullable=True)
    description = Column(Text, nullable=True)
    founder = Column(String(100), nullable=True)
    established_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    def __repr__(self):
        return f"<Clan {self.name}>"


class AncestorData(SQLAlchemyBase):
    """祖上资料模型"""
    __tablename__ = "ancestor_data"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False, index=True)
    surname = Column(String(20), nullable=False, index=True)
    hall_name = Column(String(100), nullable=True, index=True)
    ancestor_name = Column(String(100), nullable=True)
    origin = Column(String(200), nullable=True)
    description = Column(Text, nullable=True)
    status = Column(Enum(AncestorDataStatus), default=AncestorDataStatus.PENDING, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    def __repr__(self):
        return f"<AncestorData {self.id}>"


class Application(SQLAlchemyBase):
    """认祖申请模型"""
    __tablename__ = "applications"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False, index=True)
    ancestor_data_id = Column(String, ForeignKey("ancestor_data.id"), nullable=False)
    clan_id = Column(String, ForeignKey("clans.id"), nullable=False, index=True)
    status = Column(Enum(ApplicationStatus), default=ApplicationStatus.PENDING, nullable=False)
    reason = Column(Text, nullable=True)
    review_notes = Column(Text, nullable=True)
    reviewed_by = Column(String, ForeignKey("users.id"), nullable=True)
    reviewed_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    def __repr__(self):
        return f"<Application {self.id}>"


class Match(SQLAlchemyBase):
    """匹配结果模型"""
    __tablename__ = "matches"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    ancestor_data_id = Column(String, ForeignKey("ancestor_data.id"), nullable=False, index=True)
    clan_id = Column(String, ForeignKey("clans.id"), nullable=False, index=True)
    match_score = Column(String, nullable=False)  # 匹配分数
    match_reasons = Column(Text, nullable=True)  # 匹配原因
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    def __repr__(self):
        return f"<Match {self.id}>"
