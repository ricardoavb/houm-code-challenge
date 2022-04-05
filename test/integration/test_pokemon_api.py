def test_get_pokemon_type_by_name(pokemon_api_client):
    """
    The function should return a list with the corresponding pokemon types
    """
    pokemon_name = 'kakuna'
    types_list = pokemon_api_client.get_pokemon_type_by_name(pokemon_name)
    expected_types_list = ['bug', 'poison']
    assert types_list == expected_types_list


def test_get_all_pokemon(pokemon_api_client):
    """
    The function should return the pokemon names (all generations)
    """
    expected_pokemon_count = 1126
    pokemon_count = len(pokemon_api_client.get_all_pokemon_names())
    assert pokemon_count == expected_pokemon_count


def test_pokemon_name_contains_at_and_double_a(pokemon_api_client):
    """
    The function should return the number of occurrences a list of pokemon names contains
    both, twice 'a' and 'at', i.e. 'raticate' or 'latias'
    """
    matches = pokemon_api_client.get_filtered_pokemon_names_matches()
    expected_matches = 14
    assert matches == expected_matches


def test_raichu_compatible_species(pokemon_api_client):
    """
    The function should return the number of species (egg groups)
    a given pokemon is compatible with
    i.e. Raichu can interbreed with either ground pokemon or fairy pokemon
    """
    target_pokemon = 'raichu'
    egg_groups = pokemon_api_client.get_number_of_compatible_species_by_pokemon_name(
        target_pokemon)
    expected_egg_groups = 2
    assert egg_groups == expected_egg_groups


def test_biggest_and_smallest_fighting_pokemon_weight(pokemon_api_client):
    """
    The function should return a list with the weight of both,
    the biggest pokemon and the smallest pokemon i.e. [1300, 195]
    """
    weights = pokemon_api_client.get_biggest_and_smallest_pokemon_weight(
        pokemon_type='fighting')
    expected_weights_list = [1300, 195]
    assert weights == expected_weights_list
