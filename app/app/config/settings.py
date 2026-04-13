from pydantic_settings import BaseSettings
from typing import List, Optional
from functools import lru_cache


class Settings(BaseSettings):
    """应用配置类，使用环境变量和类型安全"""
    
    APP_NAME: str = "宗亲寻根·薪火相传"
    APP_ENV: str = "development"
    APP_DEBUG: bool = True
    APP_VERSION: str = "1.0.0"
    
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    SECRET_KEY: str = "your-super-secret-key-change-in-production-at-least-32-chars"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    CORS_ORIGINS: List[str] = ["http://localhost:8080", "http://localhost:3000"]
    
    DATABASE_URL: str = "sqlite:///./zongqin.db"
    MONGODB_URL: str = "mongodb://localhost:27017"
    MONGODB_DB_NAME: str = "zongqin"
    
    REDIS_URL: str = "redis://localhost:6379/0"
    
    ELASTICSEARCH_URL: str = "http://localhost:9200"
    
    S3_ACCESS_KEY: str = ""
    S3_SECRET_KEY: str = ""
    S3_REGION: str = "us-east-1"
    S3_BUCKET: str = "zongqin-storage"
    
    BCRYPT_ROUNDS: int = 12
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """获取单例配置对象"""
    return Settings()
