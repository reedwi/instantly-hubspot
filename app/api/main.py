from fastapi import APIRouter

from app.api.routes import install, accounts

api_router = APIRouter()
api_router.include_router(install.router, prefix='/install', tags=['install'])
api_router.include_router(accounts.router, prefix='/accounts', tags=['accounts'])