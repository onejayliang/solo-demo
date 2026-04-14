from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import time
from datetime import datetime
import uvicorn

from app.config.settings import get_settings
from app.api.routes import api_router
from app.api.schemas.common import ApiResponse, HealthCheckResponse

# 获取配置并确保调试模式开启
settings = get_settings()
settings.APP_DEBUG = True

app = FastAPI(
    title=settings.APP_NAME,
    description="宗亲寻根·薪火相传API (调试模式)",
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    debug=settings.APP_DEBUG
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """添加处理时间头"""
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.middleware("http")
async def security_headers(request: Request, call_next):
    """添加安全响应头"""
    response = await call_next(request)
    
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    
    if settings.APP_ENV == "production":
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    
    return response


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """全局异常处理"""
    # 在调试模式下，返回详细的错误信息
    if settings.APP_DEBUG:
        return JSONResponse(
            status_code=500,
            content=ApiResponse(
                success=False,
                message=str(exc),
                error_code="INTERNAL_ERROR",
                data={"error_details": str(exc)}
            ).model_dump()
        )
    return JSONResponse(
        status_code=500,
        content=ApiResponse(
            success=False,
            message="服务器内部错误",
            error_code="INTERNAL_ERROR"
        ).model_dump()
    )


@app.get("/health", response_model=HealthCheckResponse, tags=["健康检查"])
async def health_check():
    """健康检查端点"""
    return HealthCheckResponse(
        status="healthy",
        version=settings.APP_VERSION,
        timestamp=datetime.utcnow().isoformat(),
        services={
            "api": "healthy",
            "database": "healthy",
            "cache": "healthy"
        }
    )


@app.get("/", response_model=ApiResponse, tags=["根路径"])
async def root():
    """根路径"""
    return ApiResponse(
        success=True,
        message=f"欢迎使用{settings.APP_NAME}API (调试模式)",
        data={
            "version": settings.APP_VERSION,
            "docs": "/docs",
            "debug": settings.APP_DEBUG
        }
    )


app.include_router(api_router)

if __name__ == "__main__":
    print("=== 启动调试模式 ===")
    print(f"应用名称: {settings.APP_NAME}")
    print(f"应用版本: {settings.APP_VERSION}")
    print(f"调试模式: {settings.APP_DEBUG}")
    # 覆盖端口为7000，与前端代理配置匹配
    debug_port = 7000
    print(f"服务器地址: http://{settings.HOST}:{debug_port}")
    print(f"API文档: http://{settings.HOST}:{debug_port}/docs")
    print("==================")
    
    uvicorn.run(
        "debug:app",
        host=settings.HOST,
        port=debug_port,
        reload=settings.APP_DEBUG,
        log_level="debug",
        workers=1  # 调试模式下使用单进程
    )
