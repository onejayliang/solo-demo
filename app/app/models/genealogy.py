from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Integer, Boolean, Enum
from sqlalchemy.sql import func
from app.database.db import SQLAlchemyBase
import uuid
import enum


class GenealogyPermission(str, enum.Enum):
    """族谱权限"""
    VIEW = "view"
    EDIT = "edit"
    DOWNLOAD = "download"


class GenealogyStatus(str, enum.Enum):
    """族谱状态"""
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"


class Genealogy(SQLAlchemyBase):
    """族谱模型"""
    __tablename__ = "genealogies"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(200), nullable=False, index=True)
    clan_id = Column(String, ForeignKey("clans.id"), nullable=True, index=True)
    creator_id = Column(String, ForeignKey("users.id"), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(Enum(GenealogyStatus), default=GenealogyStatus.DRAFT, nullable=False)
    member_count = Column(Integer, default=0, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    def __repr__(self):
        return f"<Genealogy {self.name}>"


class GenealogyMember(SQLAlchemyBase):
    """族谱成员模型"""
    __tablename__ = "genealogy_members"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    genealogy_id = Column(String, ForeignKey("genealogies.id"), nullable=False, index=True)
    name = Column(String(100), nullable=False, index=True)
    gender = Column(String(10), nullable=True)
    birth_date = Column(DateTime, nullable=True)
    death_date = Column(DateTime, nullable=True)
    father_id = Column(String, ForeignKey("genealogy_members.id"), nullable=True)
    mother_id = Column(String, ForeignKey("genealogy_members.id"), nullable=True)
    spouse_id = Column(String, ForeignKey("genealogy_members.id"), nullable=True)
    generation = Column(String(50), nullable=True, index=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    def __repr__(self):
        return f"<GenealogyMember {self.name}>"


class GenealogyDocument(SQLAlchemyBase):
    """族谱文献模型"""
    __tablename__ = "genealogy_documents"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    genealogy_id = Column(String, ForeignKey("genealogies.id"), nullable=False, index=True)
    name = Column(String(200), nullable=False)
    file_path = Column(String(500), nullable=False)
    file_type = Column(String(50), nullable=True)
    size = Column(Integer, nullable=True)
    description = Column(Text, nullable=True)
    uploaded_by = Column(String, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    def __repr__(self):
        return f"<GenealogyDocument {self.name}>"


class GenealogyUserPermission(SQLAlchemyBase):
    """族谱权限模型"""
    __tablename__ = "genealogy_permissions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    genealogy_id = Column(String, ForeignKey("genealogies.id"), nullable=False, index=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False, index=True)
    permission = Column(Enum(GenealogyPermission), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    def __repr__(self):
        return f"<GenealogyUserPermission {self.permission}>"
