from fastapi import APIRouter

from app.api.endpoints import dog_routes, user_routes

api_router = APIRouter()

api_router.include_router(dog_routes.api_router, prefix="/dogs", tags=["Dog"])
api_router.include_router(user_routes.api_router, prefix="/users", tags=["User"])
