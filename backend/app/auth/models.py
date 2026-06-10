import enum
import uuid

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class UserRole(str, enum.Enum):
    ADMIN = "admin"
    COORDINADOR = "coordinador"
    MAESTRO = "maestro"


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"

    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, name="user_role"),
        default=UserRole.MAESTRO,
        nullable=False,
    )
