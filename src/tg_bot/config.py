from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    ENV: str = Field(default="dev")

    BOT_TOKEN: SecretStr = Field(default=...)
