from fastapi import APIRouter

from app.api.api_v1.endpoints.user import router as user_router

router = APIRouter()

router.include_router(user_router)
