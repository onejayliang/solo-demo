from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
import redis
from elasticsearch import Elasticsearch
from app.config.settings import get_settings

settings = get_settings()

SQLAlchemyBase = declarative_base()

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
    echo=settings.APP_DEBUG
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """获取SQLAlchemy数据库会话的依赖项"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


mongo_client = None
mongo_db = None


def get_mongo_db():
    """获取MongoDB数据库连接"""
    global mongo_client, mongo_db
    if mongo_client is None:
        mongo_client = MongoClient(settings.MONGODB_URL)
        mongo_db = mongo_client[settings.MONGODB_DB_NAME]
    return mongo_db


redis_client = None


def get_redis():
    """获取Redis连接"""
    global redis_client
    if redis_client is None:
        redis_client = redis.from_url(settings.REDIS_URL, decode_responses=True)
    return redis_client


es_client = None


def get_elasticsearch():
    """获取Elasticsearch客户端"""
    global es_client
    if es_client is None:
        es_client = Elasticsearch(settings.ELASTICSEARCH_URL)
    return es_client
