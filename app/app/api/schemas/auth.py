from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional
from datetime import datetime


class UserLogin(BaseModel):
    """用户登录请求"""
    username: str = Field(..., min_length=2, max_length=50, description="用户名")
    password: str = Field(..., min_length=1, description="密码")


class UserRegister(BaseModel):
    """用户注册请求"""
    username: str = Field(..., min_length=2, max_length=50, description="用户名")
    email: EmailStr = Field(..., description="邮箱地址")
    password: str = Field(..., min_length=8, description="密码")
    real_name: Optional[str] = Field(None, max_length=50, description="真实姓名")

    @validator('password')
    def validate_password(cls, v):
        """验证密码强度"""
        if len(v) < 8:
            raise ValueError('密码至少需要8个字符')
        if not any(c.isupper() for c in v):
            raise ValueError('密码需要包含至少一个大写字母')
        if not any(c.islower() for c in v):
            raise ValueError('密码需要包含至少一个小写字母')
        if not any(c.isdigit() for c in v):
            raise ValueError('密码需要包含至少一个数字')
        return v


class TokenResponse(BaseModel):
    """令牌响应"""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int


class UserResponse(BaseModel):
    """用户信息响应"""
    id: str
    username: str
    email: str
    real_name: Optional[str]
    surname: Optional[str]
    generation: Optional[str]
    style_name: Optional[str]
    clan_id: Optional[str]
    is_verified: bool
    is_active: bool
    bio: Optional[str]
    avatar_url: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class AuthResponse(BaseModel):
    """认证响应"""
    user: UserResponse
    tokens: TokenResponse
