from pydantic import BaseModel, Field
from typing import Generic, TypeVar, Optional, List, Any

T = TypeVar('T')


class ApiResponse(BaseModel, Generic[T]):
    """通用API响应"""
    success: bool = True
    message: Optional[str] = None
    data: Optional[T] = None
    error_code: Optional[str] = None


class PaginatedResponse(BaseModel, Generic[T]):
    """分页响应"""
    items: List[T]
    total: int
    page: int
    page_size: int
    total_pages: int


class ErrorDetail(BaseModel):
    """错误详情"""
    field: Optional[str] = None
    message: str


class ErrorResponse(BaseModel):
    """错误响应"""
    success: bool = False
    message: str
    errors: Optional[List[ErrorDetail]] = None
    error_code: Optional[str] = None


class HealthCheckResponse(BaseModel):
    """健康检查响应"""
    status: str
    version: str
    timestamp: str
    services: dict
