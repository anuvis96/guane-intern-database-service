from pydantic.main import Model
from crud.base import CRUDBase
from typing import Any, Dict, List, TypeVar, Union
from app.models.dog import Dog
from app.utils.image_dog import up_image 
from app.schemas.dog_schema import Dog_Schema, Dog_Schema_Update


class DogCrud(CRUDBase[Dog, Dog_Schema, Dog_Schema_Update]):

    async def createDog(self, dog_name):
        picture_dog = up_image()
    # Se crea el usuario admin con el cual podemos crear un primer perro
    ##id_user = await User.get(id=int(1))
    # Además se convierte id en entero para que lo tome como el id del modelo
        dog_data = Dog(dog_name=dog_name, picture=picture_dog,
                   id_user=None, is_adopted=True)
        dog_result = await self.model.create(dog_data)
        return dog_result

    async def get_by_name(self, *, dog_name: str) -> Union[dict, None]:
        model = await self.model.filter(dog_nameid=dog_name).first().values()
        if model:
            return model[0]
        return None

    async def delete_name(self, *, name: str) -> int:
        model = await self.model.filter(name=name).first().delete()
        return model      


dog_crud = DogCrud(Model=Dog)
