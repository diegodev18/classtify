import uuid

from fastapi import Depends
from fastapi_users import BaseUserManager, UUIDIDMixin

from app.auth.dependencies import get_user_db
from app.auth.models import User
from app.config import settings


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = settings.jwt_secret
    verification_token_secret = settings.jwt_secret


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
