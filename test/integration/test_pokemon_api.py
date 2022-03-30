from urllib import response
from commons.definitions import POKEMON_API_URL
import requests

def test_api_response():
    assert 10 == 10
    resource = f'{POKEMON_API_URL}pokemon/pikachu'
    response = requests.get(resource)
    print(response)
