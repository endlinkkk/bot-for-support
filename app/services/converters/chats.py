from datetime import datetime
from ddtos.messages import ChatItemDTO


def convert_chat_response_to_chat_dto(chat_data: dict) -> ChatItemDTO:
    return ChatItemDTO(
        oid=chat_data["oid"],
        title=chat_data["title"],
        created_at=datetime.fromisoformat(chat_data["created_at"]),
    )
