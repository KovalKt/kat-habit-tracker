from functools import lru_cache
from pydantic import BaseSettings, Field


class Config(BaseSettings):
    """Application settings loaded from environment variables or .env file"""

    # App settings
    APP_NAME: str = Field("Kat Habit Tracker")
    DEBUG: bool = Field(True, env="DEBUG")

    # Database settings
    DATABASE_URL: str = Field(..., env="DATABASE_URL")

    # API settings
    API_HOST: str = Field("127.0.0.1", env="API_HOST")
    API_PORT: int = Field(8000, env="API_PORT")


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache()
def get_config() -> Config:
    """Get cached settings instance"""
    return Config()
