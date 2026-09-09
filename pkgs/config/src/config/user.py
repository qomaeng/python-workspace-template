from pydantic_settings import BaseSettings, SettingsConfigDict


class UserConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="USER_",
        extra="ignore",
    )
