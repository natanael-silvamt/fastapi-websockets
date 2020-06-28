from fastapi import APIRouter
from api.endpoints.websocket import app as web_router

router = APIRouter()
router.include_router(web_router)
