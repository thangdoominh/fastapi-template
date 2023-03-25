from contextvars import ContextVar, Token
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_scoped_session,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Union

from core.config import config

session_context: ContextVar[str] = ContextVar("session_context")


def get_session_id() -> str:
    return session_context.get()


def set_session_context(session_id: str) -> Token:
    return session_context.set(session_id)


def reset_session_context(context: Token) -> None:
    session_context.reset(context)


engine = create_async_engine(config.DB_URL, pool_recycle=3600, echo=True)
try:
    conn = engine.connect()
    print("Database connection established")
except:
    print("Failed to connect to database")
finally:
    conn.close()

async_session_factory = sessionmaker(bind=engine, class_=AsyncSession)

session: Union[AsyncSession, async_scoped_session] = async_scoped_session(
    session_factory=async_session_factory,
    scopefunc=get_session_id,
)
Base = declarative_base()
