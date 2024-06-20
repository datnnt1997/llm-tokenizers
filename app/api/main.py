from fastapi import APIRouter

from app.api.routers import tokenizer, web

api_router = APIRouter()

api_router.include_router(web.router, tags=["Web"])
api_router.include_router(tokenizer.router, prefix="/tokenizer", tags=["Tokenizer"])


