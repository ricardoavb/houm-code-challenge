from commons.definitions import POKEMON_API_URL
import requests


class PokemonApiClient:
    
    def get_first_generation_pokemon_names(self):
        """
        Returns a list with all the first generation pokemon names
        """
        resource = f'{POKEMON_API_URL}pokemon?limit=151'
        response = requests.get(resource)
        response_data = response.json()
        all_pokemon = response_data['results']
        pokemon_names = list(map(lambda pokemon: pokemon['name'], all_pokemon))
        return pokemon_names

    def get_filtered_first_generation_pokemon_names_matches(self):
        """
        Returns the number of occurrences a list of pokemon names contains
        both, twice 'a' and 'at', i.e 'raticate' 
        """
        pokemon_names = self.get_first_generation_pokemon_names()
        target_occurrences = 2
        target_pattern = 'at'
        filter_criteria = lambda name: name.count('a') == target_occurrences \
            and target_pattern in name
        filtered_pokemon_names = list(filter(filter_criteria, pokemon_names))
        return len(filtered_pokemon_names)

    def get_number_of_egg_groups_by_pokemon_name(self, name):
        """
        Returns the number of species (egg groups) a given pokemon is compatible with
        """
        resource = f'{POKEMON_API_URL}pokemon-species/{name}'
        response = requests.get(resource)
        response_data = response.json()
        map_criteria = lambda egg_group: egg_group['name']
        pokemon_egg_groups = list(map(map_criteria, response_data['egg_groups']))
        return len(set(pokemon_egg_groups))
