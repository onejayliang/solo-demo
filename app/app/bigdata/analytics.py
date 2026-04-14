from typing import List, Dict, Optional
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

from app.models.ancestor_data import AncestorData, Match
from app.models.genealogy import Genealogy, GenealogyMember
from app.models.interaction import Activity, CultureShare
from app.database.db import get_db
from sqlalchemy.orm import Session


class DataAnalyzer:
    """数据分析器"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def analyze_ancestor_distribution(self) -> Dict[str, any]:
        """分析祖先数据分布"""
        # 获取所有祖先数据
        ancestor_data = self.db.query(AncestorData).all()
        
        if not ancestor_data:
            return {"message": "无祖先数据"}
        
        # 转换为DataFrame
        data = []
        for item in ancestor_data:
            data.append({
                "surname": item.surname,
                "origin_place": item.origin_place,
                "birth_year": item.birth_year,
                "generation_character": item.generation_character,
                "created_at": item.created_at
            })
        
        df = pd.DataFrame(data)
        
        # 姓氏分布
        surname_dist = df['surname'].value_counts().to_dict()
        
        # 籍贯分布
        origin_dist = df['origin_place'].value_counts().to_dict()
        
        # 年代分布
        if not df['birth_year'].isnull().all():
            year_dist = df['birth_year'].value_counts().sort_index().to_dict()
        else:
            year_dist = {}
        
        # 字辈分布
        if not df['generation_character'].isnull().all():
            generation_dist = df['generation_character'].value_counts().to_dict()
        else:
            generation_dist = {}
        
        return {
            "total_ancestors": len(ancestor_data),
            "surname_distribution": surname_dist,
            "origin_distribution": origin_dist,
            "year_distribution": year_dist,
            "generation_distribution": generation_dist
        }
    
    def analyze_match_statistics(self) -> Dict[str, any]:
        """分析匹配统计"""
        # 获取所有匹配记录
        matches = self.db.query(Match).all()
        
        if not matches:
            return {"message": "无匹配记录"}
        
        # 计算匹配相似度分布
        similarity_scores = [match.similarity_score for match in matches]
        avg_similarity = np.mean(similarity_scores) if similarity_scores else 0
        max_similarity = max(similarity_scores) if similarity_scores else 0
        min_similarity = min(similarity_scores) if similarity_scores else 0
        
        # 按相似度区间统计
        similarity_bins = {
            "high": 0,  # 0.8-1.0
            "medium": 0,  # 0.5-0.8
            "low": 0  # 0.0-0.5
        }
        
        for score in similarity_scores:
            if score >= 0.8:
                similarity_bins["high"] += 1
            elif score >= 0.5:
                similarity_bins["medium"] += 1
            else:
                similarity_bins["low"] += 1
        
        return {
            "total_matches": len(matches),
            "average_similarity": round(avg_similarity, 2),
            "max_similarity": round(max_similarity, 2),
            "min_similarity": round(min_similarity, 2),
            "similarity_distribution": similarity_bins
        }
    
    def analyze_genealogy_statistics(self) -> Dict[str, any]:
        """分析族谱统计"""
        # 获取所有族谱
        genealogies = self.db.query(Genealogy).all()
        
        if not genealogies:
            return {"message": "无族谱数据"}
        
        # 统计族谱数量和成员数量
        total_genealogies = len(genealogies)
        total_members = sum(genealogy.member_count for genealogy in genealogies)
        avg_members_per_genealogy = total_members / total_genealogies if total_genealogies > 0 else 0
        
        # 按状态统计
        status_dist = {}
        for genealogy in genealogies:
            status = genealogy.status.value if hasattr(genealogy.status, 'value') else genealogy.status
            if status not in status_dist:
                status_dist[status] = 0
            status_dist[status] += 1
        
        return {
            "total_genealogies": total_genealogies,
            "total_members": total_members,
            "average_members_per_genealogy": round(avg_members_per_genealogy, 2),
            "status_distribution": status_dist
        }
    
    def analyze_activity_statistics(self, days: int = 30) -> Dict[str, any]:
        """分析活动统计"""
        # 计算时间范围
        start_date = datetime.utcnow() - timedelta(days=days)
        
        # 获取活动数据
        activities = self.db.query(Activity).filter(
            Activity.created_at >= start_date
        ).all()
        
        if not activities:
            return {"message": "无活动数据"}
        
        # 统计活动数量和参与人数
        total_activities = len(activities)
        total_participants = sum(activity.participant_count for activity in activities)
        avg_participants_per_activity = total_participants / total_activities if total_activities > 0 else 0
        
        # 按类型统计
        # 这里假设Activity模型有type字段，如果没有可以根据实际情况调整
        type_dist = {}
        for activity in activities:
            activity_type = getattr(activity, 'type', 'unknown')
            if activity_type not in type_dist:
                type_dist[activity_type] = 0
            type_dist[activity_type] += 1
        
        return {
            "total_activities": total_activities,
            "total_participants": total_participants,
            "average_participants_per_activity": round(avg_participants_per_activity, 2),
            "type_distribution": type_dist
        }
    
    def analyze_culture_share_statistics(self, days: int = 30) -> Dict[str, any]:
        """分析文化分享统计"""
        # 计算时间范围
        start_date = datetime.utcnow() - timedelta(days=days)
        
        # 获取文化分享数据
        culture_shares = self.db.query(CultureShare).filter(
            CultureShare.created_at >= start_date
        ).all()
        
        if not culture_shares:
            return {"message": "无文化分享数据"}
        
        # 统计分享数量和点赞数
        total_shares = len(culture_shares)
        total_likes = sum(share.likes_count for share in culture_shares)
        avg_likes_per_share = total_likes / total_shares if total_shares > 0 else 0
        
        # 按宗族统计
        clan_dist = {}
        for share in culture_shares:
            clan_id = share.clan_id
            if clan_id not in clan_dist:
                clan_dist[clan_id] = 0
            clan_dist[clan_id] += 1
        
        return {
            "total_shares": total_shares,
            "total_likes": total_likes,
            "average_likes_per_share": round(avg_likes_per_share, 2),
            "clan_distribution": clan_dist
        }