from dishka import provide, Provider, Scope
from httpx import AsyncClient
from aiogram import Bot

from services.web import BaseChatWebService, ChatWebService
from settings.config import Settings


class MyProvider(Provider):
    @provide(scope=Scope.APP)
    def get_settings(self) -> Settings:
        return Settings(_env_file=".env", _env_file_encoding="utf-8")

    @provide(scope=Scope.REQUEST)
    def get_http_client(self) -> AsyncClient:
        return AsyncClient()

    @provide(scope=Scope.REQUEST)
    def get_chat_web_service(self) -> BaseChatWebService:
        return ChatWebService(
            http_client=self.get_http_client(),
            base_url=self.get_settings().web_api_base_url,
        )

    @provide(scope=Scope.REQUEST)
    def get_tg_bot(self) -> Bot:
        return Bot(
            token=self.get_settings().api_token,
        )
