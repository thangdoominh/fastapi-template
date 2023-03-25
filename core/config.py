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
    # TODO: update the url
    username: str = os.getenv("POSTGRES_USER")
    password: str = os.getenv("POSTGRES_PASSWORD")
    host: str = os.getenv("POSTGRES_HOST")
    port: int = os.getenv("POSTGRES_PORT")
    db_schema: str = os.getenv('POSTGRES_SCHEMA')
    database_name: str = os.getenv("POSTGRES_DB")
    # url postgres
    DB_URL: str = f"postgresql+asyncpg://{username}:{password}@{host}:{port}/{database_name}?search_path={db_schema}"


class DevelopmentConfig(Config):
    # DB_URL: str = f"mysql+aiomysql://root:fastapi@db:3306/fastapi"
    pass


class LocalConfig(Config):
    # TODO: update the url
    # ENV = "local"
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
    print("test >>>", config_type[env])
    return config_type[env]


config = get_config()
