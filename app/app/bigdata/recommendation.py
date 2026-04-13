from typing import List, Dict, Optional
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

from app.models.ancestor_data import AncestorData, Match
from app.models.genealogy import Genealogy, GenealogyMember
from app.models.interaction import Activity, CultureShare, ActivityParticipant
from app.models.user import User
from app.database.db import get_db
from sqlalchemy.orm import Session


class RecommendationEngine:
    """推荐引擎"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def recommend_ancestors(self, user_id: str, limit: int = 5) -> List[AncestorData]:
        """推荐可能相关的祖先数据"""
        # 获取用户创建的祖先数据
        user_ancestors = self.db.query(AncestorData).filter(
            AncestorData.user_id == user_id
        ).all()
        
        if not user_ancestors:
            # 如果用户没有创建祖先数据，返回热门的祖先数据
            return self.db.query(AncestorData).order_by(
                AncestorData.created_at.desc()
            ).limit(limit).all()
        
        # 提取用户祖先数据的特征
        user_surnames = set(ancestor.surname for ancestor in user_ancestors)
        user_origins = set(ancestor.origin_place for ancestor in user_ancestors if ancestor.origin_place)
        
        # 查找具有相同姓氏或籍贯的祖先数据
        recommended = self.db.query(AncestorData).filter(
            AncestorData.user_id != user_id,
            AncestorData.surname.in_(user_surnames) | AncestorData.origin_place.in_(user_origins)
        ).order_by(
            AncestorData.created_at.desc()
        ).limit(limit).all()
        
        return recommended
    
    def recommend_genealogies(self, user_id: str, limit: int = 5) -> List[Genealogy]:
        """推荐可能相关的族谱"""
        # 获取用户参与的族谱
        user_permissions = self.db.query(GenealogyUserPermission).filter(
            GenealogyUserPermission.user_id == user_id
        ).all()
        
        user_genealogy_ids = set(perm.genealogy_id for perm in user_permissions)
        
        # 获取用户创建的族谱
        user_created_genealogies = self.db.query(Genealogy).filter(
            Genealogy.creator_id == user_id
        ).all()
        
        for genealogy in user_created_genealogies:
            user_genealogy_ids.add(genealogy.id)
        
        # 查找用户未参与但可能相关的族谱
        # 基于姓氏和籍贯匹配
        user_ancestors = self.db.query(AncestorData).filter(
            AncestorData.user_id == user_id
        ).all()
        
        user_surnames = set(ancestor.surname for ancestor in user_ancestors)
        
        recommended = self.db.query(Genealogy).filter(
            ~Genealogy.id.in_(user_genealogy_ids),
            Genealogy.status == "published"
        ).all()
        
        # 根据姓氏匹配度排序
        def get_match_score(genealogy):
            # 这里可以根据实际情况实现更复杂的匹配算法
            # 简单实现：检查族谱名称是否包含用户的姓氏
            for surname in user_surnames:
                if surname in genealogy.name:
                    return 1
            return 0
        
        recommended.sort(key=get_match_score, reverse=True)
        
        return recommended[:limit]
    
    def recommend_activities(self, user_id: str, limit: int = 5) -> List[Activity]:
        """推荐可能感兴趣的活动"""
        # 获取用户参与的活动
        user_participations = self.db.query(ActivityParticipant).filter(
            ActivityParticipant.user_id == user_id
        ).all()
        
        user_activity_ids = set(participation.activity_id for participation in user_participations)
        
        # 获取用户的宗族
        user_ancestors = self.db.query(AncestorData).filter(
            AncestorData.user_id == user_id
        ).all()
        
        user_clan_ids = set(ancestor.clan_id for ancestor in user_ancestors if ancestor.clan_id)
        
        # 查找用户未参与但可能感兴趣的活动
        recommended = self.db.query(Activity).filter(
            ~Activity.id.in_(user_activity_ids),
            Activity.status == "upcoming",
            Activity.start_time > datetime.utcnow()
        ).all()
        
        # 根据宗族匹配度和时间排序
        def get_activity_score(activity):
            score = 0
            if activity.clan_id in user_clan_ids:
                score += 1
            # 时间越近，分数越高
            time_diff = (activity.start_time - datetime.utcnow()).total_seconds()
            if time_diff > 0:
                score += 1 / (time_diff / 3600 / 24)  # 每天递减1分
            return score
        
        recommended.sort(key=get_activity_score, reverse=True)
        
        return recommended[:limit]
    
    def recommend_culture_shares(self, user_id: str, limit: int = 5) -> List[CultureShare]:
        """推荐可能感兴趣的文化分享"""
        # 获取用户的宗族
        user_ancestors = self.db.query(AncestorData).filter(
            AncestorData.user_id == user_id
        ).all()
        
        user_clan_ids = set(ancestor.clan_id for ancestor in user_ancestors if ancestor.clan_id)
        
        # 查找用户宗族的文化分享，按点赞数排序
        recommended = self.db.query(CultureShare).filter(
            CultureShare.clan_id.in_(user_clan_ids)
        ).order_by(
            CultureShare.likes_count.desc(),
            CultureShare.created_at.desc()
        ).limit(limit).all()
        
        if len(recommended) < limit:
            # 如果宗族内的分享不足，添加热门分享
            remaining = limit - len(recommended)
            popular_shares = self.db.query(CultureShare).filter(
                ~CultureShare.clan_id.in_(user_clan_ids)
            ).order_by(
                CultureShare.likes_count.desc(),
                CultureShare.created_at.desc()
            ).limit(remaining).all()
            
            recommended.extend(popular_shares)
        
        return recommended
    
    def get_personalized_recommendations(self, user_id: str) -> Dict[str, List]:
        """获取个性化推荐"""
        return {
            "ancestors": self.recommend_ancestors(user_id),
            "genealogies": self.recommend_genealogies(user_id),
            "activities": self.recommend_activities(user_id),
            "culture_shares": self.recommend_culture_shares(user_id)
        }


# 补充缺失的导入
from app.models.genealogy import GenealogyUserPermission