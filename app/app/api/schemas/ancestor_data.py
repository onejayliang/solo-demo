from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from app.models.ancestor_data import AncestorDataStatus, ApplicationStatus


class AncestorDataCreate(BaseModel):
    """创建祖上资料"""
    surname: str = Field(..., min_length=1, max_length=20, description="姓氏")
    hall_name: Optional[str] = Field(None, max_length=100, description="堂号")
    ancestor_name: Optional[str] = Field(None, max_length=100, description="始祖姓名")
    origin: Optional[str] = Field(None, max_length=200, description="发源地")
    description: Optional[str] = Field(None, description="详细描述")


class AncestorDataUpdate(BaseModel):
    """更新祖上资料"""
    surname: Optional[str] = Field(None, min_length=1, max_length=20)
    hall_name: Optional[str] = Field(None, max_length=100)
    ancestor_name: Optional[str] = Field(None, max_length=100)
    origin: Optional[str] = Field(None, max_length=200)
    description: Optional[str] = Field(None)


class AncestorDataResponse(BaseModel):
    """祖上资料响应"""
    id: str
    user_id: str
    surname: str
    hall_name: Optional[str]
    ancestor_name: Optional[str]
    origin: Optional[str]
    description: Optional[str]
    status: AncestorDataStatus
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class ApplicationCreate(BaseModel):
    """创建认祖申请"""
    ancestor_data_id: str = Field(..., description="祖上资料ID")
    clan_id: str = Field(..., description="宗族ID")
    reason: Optional[str] = Field(None, description="申请理由")


class ApplicationReview(BaseModel):
    """审核认祖申请"""
    status: ApplicationStatus = Field(..., description="审核状态")
    review_notes: Optional[str] = Field(None, description="审核备注")


class ApplicationResponse(BaseModel):
    """认祖申请响应"""
    id: str
    user_id: str
    ancestor_data_id: str
    clan_id: str
    status: ApplicationStatus
    reason: Optional[str]
    review_notes: Optional[str]
    reviewed_by: Optional[str]
    reviewed_at: Optional[datetime]
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class MatchResponse(BaseModel):
    """匹配结果响应"""
    id: str
    ancestor_data_id: str
    clan_id: str
    clan_name: str
    match_score: str
    match_reasons: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class StyleNameRequest(BaseModel):
    """生成表字请求"""
    name: str = Field(..., description="姓名")
    clan_id: Optional[str] = Field(None, description="宗族ID")
    generation: Optional[str] = Field(None, description="辈分")


class StyleNameResponse(BaseModel):
    """表字生成响应"""
    style_name: str = Field(..., description="表字")
    explanation: Optional[str] = Field(None, description="表字解释")
