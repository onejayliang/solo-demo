from typing import List, Dict, Optional
import pymongo
from elasticsearch import Elasticsearch
import json
from datetime import datetime

from app.config.settings import get_settings

settings = get_settings()


class BigDataStorage:
    """大数据存储管理器"""
    
    def __init__(self):
        self.mongodb_client = None
        self.elasticsearch_client = None
        self._connect()
    
    def _connect(self):
        """建立数据库连接"""
        # 连接MongoDB
        try:
            self.mongodb_client = pymongo.MongoClient(
                settings.MONGODB_URL,
                serverSelectionTimeoutMS=5000
            )
            # 测试连接
            self.mongodb_client.admin.command('ping')
            self.mongodb_db = self.mongodb_client[settings.MONGODB_DB]
        except Exception as e:
            print(f"MongoDB连接失败: {e}")
            self.mongodb_client = None
        
        # 连接Elasticsearch
        try:
            self.elasticsearch_client = Elasticsearch(
                settings.ELASTICSEARCH_URL,
                timeout=10
            )
            # 测试连接
            if not self.elasticsearch_client.ping():
                raise Exception("Elasticsearch连接失败")
        except Exception as e:
            print(f"Elasticsearch连接失败: {e}")
            self.elasticsearch_client = None
    
    def store_ancestor_data(self, ancestor_data: Dict) -> bool:
        """存储祖先数据到MongoDB"""
        if not self.mongodb_client:
            return False
        
        try:
            collection = self.mongodb_db['ancestor_data']
            # 添加时间戳
            ancestor_data['created_at'] = datetime.utcnow()
            ancestor_data['updated_at'] = datetime.utcnow()
            
            result = collection.insert_one(ancestor_data)
            return result.acknowledged
        except Exception as e:
            print(f"存储祖先数据失败: {e}")
            return False
    
    def store_genealogy_data(self, genealogy_data: Dict) -> bool:
        """存储族谱数据到MongoDB"""
        if not self.mongodb_client:
            return False
        
        try:
            collection = self.mongodb_db['genealogy']
            # 添加时间戳
            genealogy_data['created_at'] = datetime.utcnow()
            genealogy_data['updated_at'] = datetime.utcnow()
            
            result = collection.insert_one(genealogy_data)
            return result.acknowledged
        except Exception as e:
            print(f"存储族谱数据失败: {e}")
            return False
    
    def index_ancestor_data(self, ancestor_data: Dict) -> bool:
        """索引祖先数据到Elasticsearch"""
        if not self.elasticsearch_client:
            return False
        
        try:
            # 准备索引数据
            index_data = {
                'id': ancestor_data.get('id'),
                'surname': ancestor_data.get('surname'),
                'name': ancestor_data.get('name'),
                'origin_place': ancestor_data.get('origin_place'),
                'birth_year': ancestor_data.get('birth_year'),
                'death_year': ancestor_data.get('death_year'),
                'generation_character': ancestor_data.get('generation_character'),
                'occupation': ancestor_data.get('occupation'),
                'achievements': ancestor_data.get('achievements'),
                'description': ancestor_data.get('description'),
                'user_id': ancestor_data.get('user_id'),
                'clan_id': ancestor_data.get('clan_id'),
                'created_at': ancestor_data.get('created_at')
            }
            
            # 索引数据
            response = self.elasticsearch_client.index(
                index='ancestor_data',
                id=ancestor_data.get('id'),
                body=index_data
            )
            
            return response['result'] in ['created', 'updated']
        except Exception as e:
            print(f"索引祖先数据失败: {e}")
            return False
    
    def index_genealogy_data(self, genealogy_data: Dict) -> bool:
        """索引族谱数据到Elasticsearch"""
        if not self.elasticsearch_client:
            return False
        
        try:
            # 准备索引数据
            index_data = {
                'id': genealogy_data.get('id'),
                'name': genealogy_data.get('name'),
                'clan_id': genealogy_data.get('clan_id'),
                'description': genealogy_data.get('description'),
                'creator_id': genealogy_data.get('creator_id'),
                'member_count': genealogy_data.get('member_count'),
                'status': genealogy_data.get('status'),
                'created_at': genealogy_data.get('created_at')
            }
            
            # 索引数据
            response = self.elasticsearch_client.index(
                index='genealogy',
                id=genealogy_data.get('id'),
                body=index_data
            )
            
            return response['result'] in ['created', 'updated']
        except Exception as e:
            print(f"索引族谱数据失败: {e}")
            return False
    
    def search_ancestors(self, query: str, size: int = 10) -> List[Dict]:
        """在Elasticsearch中搜索祖先数据"""
        if not self.elasticsearch_client:
            return []
        
        try:
            search_body = {
                'query': {
                    'multi_match': {
                        'query': query,
                        'fields': ['surname', 'name', 'origin_place', 'occupation', 'achievements', 'description']
                    }
                },
                'size': size
            }
            
            response = self.elasticsearch_client.search(
                index='ancestor_data',
                body=search_body
            )
            
            results = []
            for hit in response['hits']['hits']:
                results.append(hit['_source'])
            
            return results
        except Exception as e:
            print(f"搜索祖先数据失败: {e}")
            return []
    
    def search_genealogies(self, query: str, size: int = 10) -> List[Dict]:
        """在Elasticsearch中搜索族谱数据"""
        if not self.elasticsearch_client:
            return []
        
        try:
            search_body = {
                'query': {
                    'multi_match': {
                        'query': query,
                        'fields': ['name', 'description']
                    }
                },
                'size': size
            }
            
            response = self.elasticsearch_client.search(
                index='genealogy',
                body=search_body
            )
            
            results = []
            for hit in response['hits']['hits']:
                results.append(hit['_source'])
            
            return results
        except Exception as e:
            print(f"搜索族谱数据失败: {e}")
            return []
    
    def get_ancestor_statistics(self) -> Dict:
        """获取祖先数据统计信息"""
        if not self.mongodb_client:
            return {}
        
        try:
            collection = self.mongodb_db['ancestor_data']
            
            # 姓氏分布
            surname_dist = collection.aggregate([
                {'$group': {'_id': '$surname', 'count': {'$sum': 1}}},
                {'$sort': {'count': -1}}
            ])
            
            # 籍贯分布
            origin_dist = collection.aggregate([
                {'$match': {'origin_place': {'$ne': None}}},
                {'$group': {'_id': '$origin_place', 'count': {'$sum': 1}}},
                {'$sort': {'count': -1}},
                {'$limit': 10}
            ])
            
            # 年代分布
            year_dist = collection.aggregate([
                {'$match': {'birth_year': {'$ne': None}}},
                {'$group': {'_id': '$birth_year', 'count': {'$sum': 1}}},
                {'$sort': {'_id': 1}}
            ])
            
            return {
                'surname_distribution': {item['_id']: item['count'] for item in surname_dist},
                'origin_distribution': {item['_id']: item['count'] for item in origin_dist},
                'year_distribution': {item['_id']: item['count'] for item in year_dist}
            }
        except Exception as e:
            print(f"获取祖先数据统计失败: {e}")
            return {}
    
    def close_connections(self):
        """关闭数据库连接"""
        if self.mongodb_client:
            self.mongodb_client.close()
        if self.elasticsearch_client:
            self.elasticsearch_client.close()


# 单例模式
big_data_storage = BigDataStorage()