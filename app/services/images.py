from app.models.dog import Dog
from app.schemas.dog_schema import Dog_Schema_Update
import requests


class ImageService:

    def up_image():  # Consumir Api: una url de texto
        url = "https://dog.ceo/api/breeds/image/random."
        response = requests.get(url)
        return response



image_service = ImageService()
