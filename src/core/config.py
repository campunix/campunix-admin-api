from typing import Any

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings

from src.core.constants import Environment

from dotenv import load_dotenv

load_dotenv()

class Config(BaseSettings):
    APP_VERSION: str = "1"
    SITE_DOMAIN: str = "myapp.com"
    ENVIRONMENT: Environment = Environment.PRODUCTION
    DATABASE_URL: PostgresDsn
    CORS_ORIGINS: list[str]
    CORS_ORIGINS_REGEX: str | None = None
    CORS_HEADERS: list[str]

    # find query
    PAGE: int = 1
    PAGE_SIZE: int = 20
    ORDERING: str = "-id"

settings = Config()

app_configs: dict[str, Any] = {"title": "CAMPUNIX"}
if settings.ENVIRONMENT.is_deployed:
    app_configs["root_path"] = f"/v{settings.APP_VERSION}"

if not settings.ENVIRONMENT.is_debug:
    app_configs["openapi_url"] = None  # hide docs
