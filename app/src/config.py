"""
Application configuration.

This module centralizes all application configuration and loads values
from environment variables. The rest of the application should import
configuration from here instead of reading environment variables directly.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv

# Load variables from the local .env file (development only).
load_dotenv()

class Config:
    """
    Base configuration shared across all environments.
    """

    # Flask
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    # Database
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/platform",
    )

    # Redis
    REDIS_URL = os.getenv(
        "REDIS_URL",
        "redis://localhost:6379/0",
    )

    # Application
    APP_NAME = "Secure Software Delivery Platform"
    API_VERSION = "v1" 