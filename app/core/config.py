# BaseSettings reads configuration from environment variables and validates it using Pydantic.

# When our application starts, it looks for DATABASE_URL in .env or the environment.

# If the value is missing, Pydantic raises a validation error rather than allowing the application to run with an undefined database URL.

# That's fail-fast configuration validation.

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()