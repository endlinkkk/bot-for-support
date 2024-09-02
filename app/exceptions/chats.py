from dataclasses import dataclass

from exceptions.base import ApplicationException


@dataclass(eq=False)
class ChatListRequestError(ApplicationException):
    status_code: int
    response_content: str

    @property
    def message(self):
        return "Failed to get chat list"


@dataclass(eq=False)
class ListenerListRequestError(ApplicationException):
    status_code: int
    response_content: str

    @property
    def message(self):
        return "Failed to get chat listeners"


@dataclass(eq=False)
class ListenerAddRequestError(ApplicationException):
    status_code: int
    response_content: str

    @property
    def message(self):
        return "Failed to add chat listeners"



@dataclass(eq=False)
class ChatInfoRequestError(ApplicationException):
    status_code: int
    response_content: str

    @property
    def message(self):
        return "Failed to get chat information"