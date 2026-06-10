from fastapi import APIRouter

from app.api.v1 import health
from app.auth.router import auth_router, register_router, users_router

api_v1_router = APIRouter(prefix="/api/v1")

api_v1_router.include_router(health.router, tags=["health"])
api_v1_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_v1_router.include_router(register_router, prefix="/auth", tags=["auth"])
api_v1_router.include_router(users_router, prefix="/auth/users", tags=["users"])
