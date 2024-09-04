from datetime import datetime
from ddtos.messages import ChatItemDTO, ChatListenerDTO


def convert_chat_response_to_chat_dto(chat_data: dict) -> ChatItemDTO:
    return ChatItemDTO(
        oid=chat_data["oid"],
        title=chat_data["title"],
        created_at=datetime.fromisoformat(chat_data["created_at"]),
    )


def conver_chat_listener_response_to_listener_dto(
    listener_data: dict,
) -> ChatListenerDTO:
    return ChatListenerDTO(oid=listener_data["oid"])
