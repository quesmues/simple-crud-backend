import logging
import os
import pathlib

from dotenv import load_dotenv
from pydantic import BaseSettings

filepath = pathlib.Path(__file__).resolve().parent.parent

load_dotenv(str(filepath) + "/.env")


class Settings(BaseSettings):
    debug: bool = os.getenv("DEBUG")
    app_name: str = "Simple Crud Python"
    prefix_v1: str = "/api/v1"

    sqlalchemy_db_url: str = os.getenv("DATABASE_URL")

    cors_allow_origins: str = os.getenv("CORS_ALLOW_ORGINS")

    jwt_configs: dict = {
        "ACCESS_TOKEN_EXPIRE_MINUTES": 30,  # 30 minutos
        "REFRESH_TOKEN_EXPIRE_MINUTES": 60 * 24 * 7,  # 7 dias
        "ALGORITHM": "HS256",
        "JWT_SECRET_KEY": os.getenv("JWT_SECRET_KEY"),
        "JWT_REFRESH_SECRET_KEY": os.getenv("JWT_REFRESH_SECRET_KEY"),
    }


settings = Settings()

if settings.debug:
    logging.basicConfig(level=logging.DEBUG)
