"""
=========================================================
Module: config.py

Purpose:
    Central application configuration.

Responsibilities:
    - Database settings
    - JWT configuration
    - Security configuration

=========================================================
"""

from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    """
    Application settings.
    """

    DATABASE_URL: str = "sqlite:///./farm_activity_planner.db"

    SECRET_KEY: str = (
        "replace-this-with-a-long-random-secret-key"
    )

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()