from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import join
from typing import List

from app.database.db import get_db
from app.models.ancestor_data import AncestorData, Match, Clan
from app.api.schemas.ancestor_data import (
    MatchResponse, StyleNameRequest, StyleNameResponse
)
from app.api.controllers.auth import get_current_active_user
from app.models.user import User

router = APIRouter(prefix="/match", tags=["匹配服务"])


@router.get("/relatives/{data_id}", response_model=List[MatchResponse])
def match_relatives(
    data_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """宗亲匹配"""
    # 验证资料归属
    ancestor_data = db.query(AncestorData).filter(
        AncestorData.id == data_id
    ).first()
    
    if not ancestor_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="资料不存在"
        )
    
    if ancestor_data.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权限访问"
        )
    
    # 查询匹配结果，关联宗族信息
    matches = db.query(
        Match,
        Clan.name.label('clan_name')
    ).join(
        Clan, Match.clan_id == Clan.id
    ).filter(
        Match.ancestor_data_id == data_id
    ).order_by(
        Match.match_score.desc()
    ).all()
    
    # 构建响应数据
    result = []
    for match, clan_name in matches:
        result.append(MatchResponse(
            id=match.id,
            ancestor_data_id=match.ancestor_data_id,
            clan_id=match.clan_id,
            clan_name=clan_name,
            match_score=match.match_score,
            match_reasons=match.match_reasons,
            created_at=match.created_at
        ))
    
    return result


@router.post("/generate-style-name", response_model=StyleNameResponse)
def generate_style_name(
    request: StyleNameRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """生成表字"""
    # 这里可以实现表字生成的逻辑
    # 简单示例：根据姓名和辈分生成表字
    import random
    
    # 表字库
    style_words = [
        "明", "德", "仁", "义", "礼", "智", "信",
        "忠", "孝", "廉", "耻", "勇", "毅", "谦",
        "和", "顺", "安", "宁", "康", "泰", "祥"
    ]
    
    # 生成表字
    given_name = request.name
    if len(given_name) >= 2:
        # 取名字的第二个字作为基础
        base_char = given_name[1]
    else:
        base_char = given_name[0]
    
    # 随机选择一个字
    random_word = random.choice(style_words)
    style_name = f"{base_char}{random_word}"
    
    # 生成解释
    explanation = f"表字 '{style_name}' 取自姓名 '{given_name}'，寓意吉祥如意"
    
    if request.generation:
        explanation += f"，对应辈分 '{request.generation}'"
    
    return StyleNameResponse(
        style_name=style_name,
        explanation=explanation
    )
