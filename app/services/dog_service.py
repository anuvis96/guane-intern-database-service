from typing import Any, Dict, Optional, TypeVar, Union
from app.infra.postgres.crud.dog import dog_crud
from app.schemas.dog_schema import Dog_Schema_Update, Dog_Schema


QueryType = TypeVar("QueryType", bound=dog_crud)

class DogService:
    def __init__(self, dog_queries: QueryType):
        self.__dog_queries = dog_queries

    async def get_dogs(self) -> Union[dict, None]:
        new_dogs = await self.__dog_queries.get_all()
        return new_dogs    

    async def create_dog(self, dog_name) -> Union[dict, None]:
        new_dog_id = await self.__dog_queries.createDog(dog_name=dog_name)
        return new_dog_id

    async def get_dog_by_name(self, dog_name: str) -> Union[dict, None]:
        dog = await self.__dog_queries.get_by_name(name=dog_name)
        if dog:
            return dog
        return None

    async def update_dog(
        self, dog_name: str, new_dog: Dog_Schema_Update
    ) -> Optional[Dict[int, Any]]:
        object_dog = new_dog.dict()
        current_update = await self.__dog_queries.update(
            name=dog_name, obj_in=object_dog
        )
        return current_update

    async def remove_dog(self, dog_name: str) -> int:
        dog_removed_name = await self.__dog_queries.delete(name=dog_name)
        return dog_removed_name            



dog_service = DogService(dog_queries=dog_crud)    