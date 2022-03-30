from commons.definitions import POKEMON_API_URL
import requests


class PokemonApiClient:
    
    def get_first_generation_pokemon_names(self):
        """Returns a list with all the first generation pokemon names"""
        resource = f'{POKEMON_API_URL}pokemon?limit=151'
        response = requests.get(resource)
        response_data = response.json()
        all_pokemon = response_data['results']
        pokemon_names = list(map(lambda pokemon: pokemon['name'], all_pokemon))
        return pokemon_names
