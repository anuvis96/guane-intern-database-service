from fastapi import APIRouter, Response, status
from starlette import status
from app.models.dog import Dog
from app.services.dog_service import dog_service
from app.schemas.dog_schema import Dog_Schema_Update, Dog_Schema
from app.services.dog import *
##from app.celery_worker import celery_task
from starlette.status import HTTP_204_NO_CONTENT


dog_router = APIRouter()


@dog_router.get('/dogs', tags=["dogs"])
async def get_all_dog():
    dogs = await dog_service.get_dogs()
    return dogs


@dog_router.get('/dogs/{dog_name}', tags=["dogs"])
async def find_dog(dog_name: str):
    dog = await dog_service.get_dog_by_name(dog_name)
    return dog


@dog_router.get('/is_adopted', tags=["dogs"])
async def find_dog_adopted():
    dog = await find_dog_by_adopted()
    return dog


@dog_router.post("/dogs/{dog_name}")
async def created_dog(dog_name: str):
    # Se añade la tarea que monitorea el crear dog
    dog_data = await dog_service.create_dog(dog_name)
    ##task = celery_task.send_task('app.Workers.tasks.create_order_dog')
    ##print('app.Workers.tasks.create_order_dog')  ## , task)
    return dog_data


@dog_router.put("/dogs/{dog_name}")
async def updated_dog(dog_schema: Dog_Schema_Update, dog_name: str):
    dog_data = await update_dog(dog_name=dog_name, dog_schema=dog_schema)
    return dog_data


@dog_router.delete('/dogs/{dog_name}', status_code=status.HTTP_204_NO_CONTENT, tags=["dogs"])
async def delete_dog(dog_name: str):
    dog = await Dog.filter(dog_name=dog_name).first().delete()
    if not dog:
        raise "El Dog con este Id no se encuentra."
    return f"El Dog con el Id {id} se borro exitosamente."
