from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggingConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="LOGGING_",
        extra="ignore",
    )
