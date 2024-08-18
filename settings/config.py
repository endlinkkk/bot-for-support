from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_token: str = Field(alias="API_TOKEN")


settings = Settings(_env_file='.env', _env_file_encoding='utf-8')