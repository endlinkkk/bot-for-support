from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_token: str = Field(alias="API_TOKEN")
    greeting_text: str = Field(
        alias="GREETING_TEXT",
        default="Welcome! Please select chat to work with the client.\nGet chats: /chats\nChoose Chat: /set-chats <chatoid>",
    )
    web_api_base_url: str = Field(
        alias="WEB_API_BASE_URL", default="http://127.0.0.1:8000"
    )


def get_settings() -> Settings:
    return Settings(_env_file=".env", _env_file_encoding="utf-8")
