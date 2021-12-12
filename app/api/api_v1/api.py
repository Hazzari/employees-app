from fastapi import APIRouter

from app.api.api_v1.endpoints.load_data import router as load_data
from app.api.api_v1.endpoints.user import router as user_router

router = APIRouter()

router.include_router(user_router)
router.include_router(load_data)
