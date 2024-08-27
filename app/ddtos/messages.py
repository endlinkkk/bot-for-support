from datetime import datetime
from pydantic import BaseModel


class ChatItemDTO(BaseModel):
    oid: str
    title: str
    created_at: datetime


class ChatListenerDTO(BaseModel):
    oid: str
