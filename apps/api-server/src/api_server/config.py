from ipaddress import IPv4Address
from typing import Annotated

from config import postgres
from config.logging import LoggingConfig
from config.redis import RedisConfig
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiServerConfig(BaseSettings):
    host: IPv4Address = IPv4Address("127.0.0.1")
    port: Annotated[int, Field(ge=1, le=65535)] = 8000

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="API_SERVER_",
        extra="ignore",
    )


class Config(BaseSettings):
    api_server = ApiServerConfig

    logging = LoggingConfig
    redis = RedisConfig
    postgres = postgres.PostgresConfig
