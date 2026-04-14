from fastapi import APIRouter

from app.api.v1.habits import router as habits_router
from app.api.v1.health import router as health_router
from app.api.v1.logs import router as logs_router


api_router = APIRouter()
api_router.include_router(health_router, tags=["health"])
api_router.include_router(habits_router, prefix="/api/v1/habits", tags=["habits"])
api_router.include_router(logs_router, prefix="/api/v1/logs", tags=["habit-logs"])
