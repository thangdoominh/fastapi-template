from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from core.config import config
from api import router
from api.health_check.health_check import health_check_router
from core.exceptions import CustomException
from core.middlewares import SQLAlchemyMiddleware


def init_cors(_app: FastAPI) -> None:
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def init_routers(_app: FastAPI) -> None:
    _app.include_router(health_check_router)
    _app.include_router(router)


def init_listeners(_app: FastAPI) -> None:
    # Exception handler
    @_app.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )


def init_middleware(_app: FastAPI) -> None:
    _app.add_middleware(SQLAlchemyMiddleware)


def create_app() -> FastAPI:
    _app = FastAPI(
        title="Hide",
        description="Hide API",
        version="1.0.0",
        docs_url=None if config.ENV == "production" else "/docs",
        redoc_url=None if config.ENV == "production" else "/redoc",
    )
    init_routers(_app=_app)
    init_cors(_app=_app)
    init_listeners(_app=_app)
    init_middleware(_app=_app)

    return _app


app = create_app()
