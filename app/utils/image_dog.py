import requests

def up_image():  # Consumir Api: una url de texto
    url = "https://dog.ceo/api/breeds/image/random."
    response = requests.get(url)
    return response