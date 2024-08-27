from pydantic import BaseModel


class NewChatMessageSchema(BaseModel):
    event_id: str
    occured_at: str
    message_text: str
    message_oid: str
    chat_oid: str
