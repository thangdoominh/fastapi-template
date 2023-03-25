import os

from pydantic import BaseSettings

import dotenv
import asyncio

dotenv.load_dotenv()


class Config(BaseSettings):
    ENV: str = "local"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    username: str = os.getenv("POSTGRES_USER")
    password: str = os.getenv("POSTGRES_PASSWORD")
    host: str = os.getenv("POSTGRES_HOST")
    port: int = os.getenv("POSTGRES_PORT")
    db_schema: str = os.getenv('POSTGRES_SCHEMA')
    database_name: str = os.getenv("POSTGRES_DB")
    # url postgres
    DB_URL: str = f"postgresql+asyncpg://{username}:{password}@{host}:{port}/{database_name}"


class DevelopmentConfig(Config):
    pass


class LocalConfig(Config):
    pass


class ProductionConfig(Config):
    DEBUG: str = False


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "local": LocalConfig(),
        "development": DevelopmentConfig(),
        "production": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
