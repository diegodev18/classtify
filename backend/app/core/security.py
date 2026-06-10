from fastapi import Depends, HTTPException, status

from app.auth.models import User, UserRole
from app.auth.router import current_active_user


def require_role(*roles: UserRole):
    async def checker(user: User = Depends(current_active_user)) -> User:
        if user.role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions",
            )
        return user

    return checker
