import uuid
from collections.abc import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase

from app.auth.models import User
from app.db.session import get_async_session


async def get_user_db() -> AsyncGenerator[SQLAlchemyUserDatabase, None]:
    async for session in get_async_session():
        yield SQLAlchemyUserDatabase(session, User)
