import uuid

from fastapi_users import schemas
from pydantic import EmailStr

from app.auth.models import UserRole


class UserRead(schemas.BaseUser[uuid.UUID]):
    role: UserRole


class UserCreate(schemas.BaseUserCreate):
    role: UserRole = UserRole.MAESTRO


class UserUpdate(schemas.BaseUserUpdate):
    role: UserRole | None = None
