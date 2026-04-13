from datetime import datetime, timedelta
from typing import Optional, Union
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.config.settings import get_settings

settings = get_settings()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """验证密码，防止时序攻击"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """安全地哈希密码，使用bcrypt算法"""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """创建访问令牌，包含过期时间"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire, "type": "access"})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """创建刷新令牌，更长的有效期"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    
    to_encode.update({"exp": expire, "type": "refresh"})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def decode_token(token: str) -> Optional[dict]:
    """安全解码JWT令牌，验证签名和过期时间"""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None


def validate_password_strength(password: str) -> tuple[bool, list[str]]:
    """验证密码强度，返回是否有效和错误列表"""
    errors = []
    
    if len(password) < 8:
        errors.append("密码至少需要8个字符")
    
    if not any(c.isupper() for c in password):
        errors.append("密码需要包含至少一个大写字母")
    
    if not any(c.islower() for c in password):
        errors.append("密码需要包含至少一个小写字母")
    
    if not any(c.isdigit() for c in password):
        errors.append("密码需要包含至少一个数字")
    
    if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        errors.append("密码需要包含至少一个特殊字符")
    
    return len(errors) == 0, errors


def sanitize_input(input_string: str) -> str:
    """清理用户输入，防止注入攻击"""
    if not input_string:
        return ""
    
    dangerous_chars = ["<", ">", "\"", "'", ";", "--", "/*", "*/", "@", "`", "$"]
    result = input_string
    for char in dangerous_chars:
        result = result.replace(char, "")
    
    return result.strip()
