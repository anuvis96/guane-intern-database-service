from fastapi import APIRouter, status
from starlette import status
from app.schemas.user_schema import In_User_Schema, Out_User_Schema
from app.models.user import User
from app.services.user import *
from starlette.status import HTTP_204_NO_CONTENT

user_router = APIRouter()


@user_router.get('/users', tags=["users"])
async def get_all_users_data():
    users = await get_all_users()
    return users


@user_router.get('/users/{id}', tags=["users"])
async def find_user(id: int):
    user = await find_user_by_id(id=id)
    return user


@user_router.post("/users")
async def create_users(users: In_User_Schema):
    user_data = await create_user(users=users)
    return user_data


@user_router.put("/users/{id}", response_model=Out_User_Schema)
async def update_users(id: str, user_schema: Out_User_Schema):
    user_data = await update_user(id=id, user_schema=user_schema)
    return user_data


@user_router.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
async def delete_user(id: int):
    user = await User.filter(id=id).first().delete()
    if not user:
        raise "El Usuario con este Id no se encuentra."
    return f"El Usuario con el Id {id} se borro exitosamente."
