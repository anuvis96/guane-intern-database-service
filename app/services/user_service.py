from typing import Any, Dict, Optional, TypeVar, Union
from app.infra.postgres.crud.user import user_crud
from app.schemas.user_schema import In_User_Schema, Out_User_Schema


QueryType = TypeVar("QueryType", bound=user_crud)

class UserService:
    def __init__(self, user_queries: QueryType):
        self.__user_queries = user_queries

    ##async def get_users(self) -> Union[dict, None]:
       ## new_dogs = await self.__user_queries.get_all()
        ##return new_dogs    

    async def create_user(self, user_id) -> Union[dict, None]:
        new_user_id = await self.__user_queries.createDog(id=user_id)
        return new_user_id
    
    async def get_user_by_id(self, user_id: int) -> Union[dict, None]:
        user = await self.__user_queries.get_by_id(id=user_id)
        if user:
            return user
        return None

    async def update_user(
        self, id_user: int, new_user: In_User_Schema
    ) -> Optional[Dict[int, Any]]:
        object_user = new_user.dict()
        current_update = await self.__user_queries.update(
            id=id_user, obj_in=object_user
        )
        return current_update

    async def remove_user(self, id: int) -> int:
        user_removed_id = await self.__user_queries.delete(id=id)
        return user_removed_id            



dog_service = UserService(user_queries=user_crud)    