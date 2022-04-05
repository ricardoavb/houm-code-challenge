from commons.definitions import POKEMON_API_URL
import requests


class PokemonApiClient:

    def get_all_pokemon_names(self):
        """
        Returns a list with all generations pokemon names
        """
        resource = f'{POKEMON_API_URL}pokemon'
        response = requests.get(resource)
        response_data = response.json()
        pokemon_data = response_data['results']

        while response_data['next']:
            response_data = requests.get(response_data['next']).json()
            pokemon_data.extend(response_data['results'])

        def map_criteria(pokemon):
            return pokemon['name']

        pokemon_names = list(map(map_criteria, pokemon_data))
        return pokemon_names

    def get_pokemon_type_by_name(self, name):
        resource = f'{POKEMON_API_URL}pokemon/{name}'
        response = requests.get(resource)
        response_data = response.json()
        return [pokemon_type['type']['name'] for pokemon_type in response_data['types']]
    
    
    def get_first_generation_pokemon_names(self, pokemon_type=None):
        """
        Returns a list with all the first generation pokemon names
        you can filter them by 'type'
        """
        resource = f'{POKEMON_API_URL}pokemon?limit=151'
        response = requests.get(resource)
        response_data = response.json()
        all_pokemon = response_data['results']

        def map_criteria(pokemon):
            return pokemon['name']

        pokemon_names = list(map(map_criteria, all_pokemon))

        if pokemon_type:
            return [pokemon_name for pokemon_name in pokemon_names
                    if self.get_pokemon_type_by_name(pokemon_name) == pokemon_type]
        return pokemon_names

    def get_filtered_first_generation_pokemon_names_matches(self):
        """
        Returns the number of occurrences a list of pokemon names contains
        both, twice 'a' and 'at', i.e 'raticate'
        """
        pokemon_names = self.get_all_pokemon_names()
        target_occurrences = 2
        target_pattern = 'at'

        def filter_criteria(name):
            return name.count(
                'a') == target_occurrences and target_pattern in name

        filtered_pokemon_names = list(filter(filter_criteria, pokemon_names))
        return len(filtered_pokemon_names)

    def get_number_of_egg_groups_by_pokemon_name(self, name):
        """
        Returns the number of species (egg groups) a given pokemon is compatible with
        """
        resource = f'{POKEMON_API_URL}pokemon-species/{name}'
        response = requests.get(resource)
        response_data = response.json()

        def map_criteria(egg_group):
            return egg_group['name']

        pokemon_egg_groups = list(
            map(map_criteria, response_data['egg_groups']))
        return len(set(pokemon_egg_groups))

    def get_pokemon_weight_by_name(self, name):
        """
        Returns the weight of a given pokemon
        """
        resource = f'{POKEMON_API_URL}pokemon/{name}'
        response = requests.get(resource)
        response_data = response.json()
        pokemon_weight = response_data['weight']
        return pokemon_weight

    def get_biggest_and_smallest_pokemon_weight(self, pokemon_type=None):
        """
        Returns a list with the smallest and the biggest pokemon weight
        """
        pokemon_names = self.get_first_generation_pokemon_names(pokemon_type=pokemon_type)
        pokemon_weights = [self.get_pokemon_weight_by_name(
            name) for name in pokemon_names]
        return [max(pokemon_weights), min(pokemon_weights)]
