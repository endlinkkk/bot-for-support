from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BaseChatService(ABC):
    @abstractmethod
    async def set_current_chat(self, chat_oid: str, telegram_chat_id: str): ...
