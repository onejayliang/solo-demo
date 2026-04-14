from typing import List, Dict, Optional
from datetime import datetime
import pandas as pd
import numpy as np
from scipy.spatial.distance import cosine

from app.models.ancestor_data import AncestorData, Match
from app.database.db import get_db
from sqlalchemy.orm import Session


class MatchEngine:
    """宗亲匹配引擎"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def calculate_similarity(self, data1: AncestorData, data2: AncestorData) -> float:
        """计算两个祖先数据的相似度"""
        # 基础信息相似度
        base_score = 0
        
        # 姓氏匹配
        if data1.surname == data2.surname:
            base_score += 0.3
        
        # 籍贯匹配
        if data1.origin_place == data2.origin_place:
            base_score += 0.2
        
        # 字辈匹配
        if data1.generation_character and data2.generation_character:
            if data1.generation_character == data2.generation_character:
                base_score += 0.2
        
        # 年代匹配（出生年份）
        if data1.birth_year and data2.birth_year:
            year_diff = abs(data1.birth_year - data2.birth_year)
            if year_diff <= 10:
                base_score += 0.2
            elif year_diff <= 50:
                base_score += 0.1
        
        # 其他信息匹配（如职业、成就等）
        if data1.occupation and data2.occupation:
            if data1.occupation == data2.occupation:
                base_score += 0.05
        
        if data1.achievements and data2.achievements:
            # 简单的文本相似度计算
            common_terms = set(data1.achievements.split()) & set(data2.achievements.split())
            if common_terms:
                base_score += 0.05
        
        return min(base_score, 1.0)
    
    def find_matches(self, data_id: str, threshold: float = 0.5) -> List[Match]:
        """寻找匹配的宗亲"""
        # 获取目标祖先数据
        target_data = self.db.query(AncestorData).filter(
            AncestorData.id == data_id
        ).first()
        
        if not target_data:
            return []
        
        # 获取同姓氏的祖先数据
        potential_matches = self.db.query(AncestorData).filter(
            AncestorData.surname == target_data.surname,
            AncestorData.id != data_id
        ).all()
        
        matches = []
        for candidate in potential_matches:
            similarity = self.calculate_similarity(target_data, candidate)
            
            if similarity >= threshold:
                # 检查是否已经存在匹配记录
                existing_match = self.db.query(Match).filter(
                    ((Match.ancestor_data_id1 == data_id) & (Match.ancestor_data_id2 == candidate.id)) |
                    ((Match.ancestor_data_id1 == candidate.id) & (Match.ancestor_data_id2 == data_id))
                ).first()
                
                if not existing_match:
                    new_match = Match(
                        ancestor_data_id1=data_id,
                        ancestor_data_id2=candidate.id,
                        similarity_score=similarity,
                        match_date=datetime.utcnow()
                    )
                    self.db.add(new_match)
                    matches.append(new_match)
        
        self.db.commit()
        return matches
    
    def batch_process(self, limit: int = 100):
        """批量处理匹配"""
        # 获取未处理的祖先数据
        unprocessed_data = self.db.query(AncestorData).filter(
            AncestorData.processed == False
        ).limit(limit).all()
        
        for data in unprocessed_data:
            self.find_matches(data.id)
            data.processed = True
        
        self.db.commit()


class StyleNameGenerator:
    """字辈生成器"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def generate_style_name(self, surname: str, generation: int, clan_id: str) -> str:
        """生成字辈"""
        # 这里可以根据宗族的字辈谱生成字辈
        # 简单实现：使用常用字辈
        common_generation_characters = [
            "仁", "义", "礼", "智", "信",
            "忠", "孝", "廉", "耻", "勇",
            "温", "良", "恭", "俭", "让"
        ]
        
        # 根据世代计算字辈索引
        index = generation % len(common_generation_characters)
        style_character = common_generation_characters[index]
        
        return f"{surname}{style_character}"
    
    def validate_style_name(self, style_name: str, surname: str, generation: int, clan_id: str) -> bool:
        """验证字辈是否正确"""
        # 简单验证：检查姓氏是否匹配
        if not style_name.startswith(surname):
            return False
        
        # 检查字辈字符是否符合宗族规范
        expected_style_character = self.generate_style_name(surname, generation, clan_id)[len(surname):]
        actual_style_character = style_name[len(surname):len(surname)+1]
        
        return actual_style_character == expected_style_character