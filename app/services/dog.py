from app.models.dog import Dog
from app.schemas.dog_schema import Dog_Schema_Update
from app.models.user import User
import requests


class DogService:
    

 async def get_all_dogs():  # Obtener todos los dogs
    dogs = await Dog.all()
    return dogs


# Obtener los dogs mediante el dog_name
async def find_dog_by_name(dog_name: str):
    dog = await Dog.filter(dog_name=dog_name).first().values()
    return dog


async def find_dog_by_adopted():  # Obtener todas las entradas donde la bandera is_adopted sea true
    dog = await Dog.filter(is_adopted=True).all()
    return dog


async def create_dog(dog_name: str):  # Ingresar un nuevo dog
    picture_dog = up_image()
    # Se crea el usuario admin con el cual podemos crear un primer perro
    id_user = await User.get(id=int(1))
    # Además se convierte id en entero para que lo tome como el id del modelo
    dog_data = Dog(dog_name=dog_name, picture=picture_dog,
                   id_user=id_user, is_adopted=True)
    await dog_data.save()
    return dog_data


def up_image():  # Consumir Api: una url de texto
    url = "https://dog.ceo/api/breeds/image/random."
    response = requests.get(url)
    return response


# Actualizar un dog existente por el nombre
async def update_dog(dog_name: str, dog_schema: Dog_Schema_Update):
    image_dog = up_image()
    dog_data = await Dog.get(dog_name=dog_name)
    dog_data.picture = image_dog
    dog_data.dog_name = dog_schema.dog_name
    dog_data.is_adopted = dog_schema.is_adopted
    dog_data.user_id = dog_schema.user
    await dog_data.save()
    return True


# Borrar los dogs mediante el dog_name
async def delete_dog_by_name(dog_name: str):
    dog = await Dog.filter(dog_name=dog_name).first().delete()
    if not dog:
        raise "El Dog con este Id no se encuentra."
    return f"El Dog con el Id {id} se borro exitosamente."


dog_service = DogService()
