from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import config
from api import router
from api.health_check.health_check import health_check_router
from core.middlewares import SQLAlchemyMiddleware


def init_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def init_routers(app: FastAPI) -> None:
    app.include_router(health_check_router)
    app.include_router(router)


def init_listeners(app: FastAPI) -> None:
    ...


def init_middleware(app: FastAPI) -> None:
    app.add_middleware(SQLAlchemyMiddleware)


def create_app() -> FastAPI:
    _app = FastAPI(
        title="Hide",
        description="Hide API",
        version="1.0.0",
        docs_url=None if config.ENV == "production" else "/docs",
        redoc_url=None if config.ENV == "production" else "/redoc",
    )
    init_routers(app=_app)
    init_cors(app=_app)
    init_listeners(app=_app)
    init_middleware(app=_app)

    return _app


app = create_app()
