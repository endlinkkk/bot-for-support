from dataclasses import dataclass

from exceptions.base import ApplicationException


@dataclass(eq=False)
class ChatListRequestError(ApplicationException):
    status_code: int
    response_content: str

    @property
    def message(self):
        return "Failed to get chat list"
