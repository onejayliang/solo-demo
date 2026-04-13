from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from app.models.genealogy import GenealogyStatus, GenealogyPermission


class GenealogyCreate(BaseModel):
    """创建族谱"""
    name: str = Field(..., min_length=1, max_length=200, description="族谱名称")
    clan_id: Optional[str] = Field(None, description="宗族ID")
    description: Optional[str] = Field(None, description="描述")


class GenealogyUpdate(BaseModel):
    """更新族谱"""
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None)
    status: Optional[GenealogyStatus] = Field(None)


class GenealogyResponse(BaseModel):
    """族谱响应"""
    id: str
    name: str
    clan_id: Optional[str]
    creator_id: str
    description: Optional[str]
    status: GenealogyStatus
    member_count: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class GenealogyMemberCreate(BaseModel):
    """创建族谱成员"""
    name: str = Field(..., min_length=1, max_length=100, description="姓名")
    gender: Optional[str] = Field(None, max_length=10, description="性别")
    birth_date: Optional[datetime] = Field(None, description="出生日期")
    death_date: Optional[datetime] = Field(None, description="去世日期")
    father_id: Optional[str] = Field(None, description="父亲ID")
    mother_id: Optional[str] = Field(None, description="母亲ID")
    spouse_id: Optional[str] = Field(None, description="配偶ID")
    generation: Optional[str] = Field(None, max_length=50, description="辈分")
    description: Optional[str] = Field(None, description="描述")


class GenealogyMemberResponse(BaseModel):
    """族谱成员响应"""
    id: str
    genealogy_id: str
    name: str
    gender: Optional[str]
    birth_date: Optional[datetime]
    death_date: Optional[datetime]
    father_id: Optional[str]
    mother_id: Optional[str]
    spouse_id: Optional[str]
    generation: Optional[str]
    description: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class GenealogyDocumentCreate(BaseModel):
    """上传族谱文献"""
    name: str = Field(..., min_length=1, max_length=200, description="文件名")
    description: Optional[str] = Field(None, description="描述")


class GenealogyDocumentResponse(BaseModel):
    """族谱文献响应"""
    id: str
    genealogy_id: str
    name: str
    file_path: str
    file_type: Optional[str]
    size: Optional[int]
    description: Optional[str]
    uploaded_by: str
    created_at: datetime

    class Config:
        from_attributes = True


class GenealogyPermissionUpdate(BaseModel):
    """更新族谱权限"""
    user_id: str = Field(..., description="用户ID")
    permission: GenealogyPermission = Field(..., description="权限")
