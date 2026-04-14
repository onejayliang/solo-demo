from fastapi import APIRouter, Depends, HTTPException, status, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from app.database.db import get_db
from app.models.interaction import ChatRoom, Message
from app.api.schemas.interaction import (
    ChatRoomResponse, MessageCreate, MessageResponse
)
from app.api.controllers.auth import get_current_active_user
from app.models.user import User

router = APIRouter(prefix="/chat", tags=["聊天室"])

# 存储WebSocket连接
active_connections = {}


@router.get("/rooms", response_model=List[ChatRoomResponse])
def get_chat_rooms(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """获取聊天室列表"""
    # 这里可以根据用户的宗族身份返回相应的聊天室
    chat_rooms = db.query(ChatRoom).all()
    return chat_rooms


@router.get("/{chat_room_id}/messages", response_model=List[MessageResponse])
def get_messages(
    chat_room_id: str,
    limit: int = 20,
    before: Optional[str] = None,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """获取聊天室消息"""
    # 验证聊天室存在
    chat_room = db.query(ChatRoom).filter(
        ChatRoom.id == chat_room_id
    ).first()
    
    if not chat_room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="聊天室不存在"
        )
    
    query = db.query(Message).filter(
        Message.chat_room_id == chat_room_id
    )
    
    if before:
        query = query.filter(Message.created_at < before)
    
    messages = query.order_by(Message.created_at.desc()).limit(limit).all()
    
    # 反转顺序，使最早的消息在前
    return list(reversed(messages))


@router.post("/{chat_room_id}/messages", response_model=MessageResponse)
def send_message(
    chat_room_id: str,
    message: MessageCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """发送消息"""
    # 验证聊天室存在
    chat_room = db.query(ChatRoom).filter(
        ChatRoom.id == chat_room_id
    ).first()
    
    if not chat_room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="聊天室不存在"
        )
    
    new_message = Message(
        chat_room_id=chat_room_id,
        user_id=current_user.id,
        content=message.content,
        message_type=message.message_type
    )
    
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    
    # 发送WebSocket消息
    if chat_room_id in active_connections:
        for connection in active_connections[chat_room_id]:
            try:
                import json
                connection.send_json({
                    "type": "message",
                    "data": {
                        "id": new_message.id,
                        "chat_room_id": new_message.chat_room_id,
                        "user_id": new_message.user_id,
                        "content": new_message.content,
                        "message_type": new_message.message_type,
                        "created_at": new_message.created_at.isoformat()
                    }
                })
            except:
                pass
    
    return new_message


@router.websocket("/ws/{chat_room_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    chat_room_id: str
):
    """WebSocket连接"""
    await websocket.accept()
    
    # 添加到活跃连接
    if chat_room_id not in active_connections:
        active_connections[chat_room_id] = []
    active_connections[chat_room_id].append(websocket)
    
    try:
        while True:
            data = await websocket.receive_json()
            # 这里可以处理收到的消息
            # 但实际消息处理应该通过HTTP API
    except WebSocketDisconnect:
        # 移除连接
        if chat_room_id in active_connections:
            active_connections[chat_room_id].remove(websocket)
            if not active_connections[chat_room_id]:
                del active_connections[chat_room_id]
