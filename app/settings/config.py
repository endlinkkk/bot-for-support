from pydantic import Field

from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    api_token: str = Field(alias="API_TOKEN")
    greeting_text: str = Field(
        alias="GREETING_TEXT",
        default="Welcome! Please select chat to work with the client.\nGet chats: /chats\nChoose Chat: /set-chats <chatoid>",
    )
    web_api_base_url: str = Field(
        alias="WEB_API_BASE_URL", default="http://127.0.0.1:8000"
    )
    api_port: str = Field(
        alias='API_PORT', default="8010"
    )
    kafka_broker_url: str = Field(alias="KAFKA_BROKER_URL", default="kafka:29092")
    new_message_topic: str = Field(alias="NEW_MESSAGE_TOPIC", default="new_messages")
    kafka_group_id: str = Field(alias="KAFKA_GROUP_ID", default="tg-bot")



def get_settings() -> Settings:
    return Settings()
