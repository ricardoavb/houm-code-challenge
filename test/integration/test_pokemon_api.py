def test_pokemon_name_contains_at_and_double_a(pokemon_api_client):
    """
    The function should return the number of occurrences a list of pokemon names contains
    both, twice 'a' and 'at', i.e. 'raticate' 
    """
    matches = pokemon_api_client.get_filtered_first_generation_pokemon_names_matches()
    expected_matches = 1
    assert matches == expected_matches

def test_raichu_compatible_species(pokemon_api_client):
    """
    The function should return the number of species (egg groups)
    a given pokemon is compatible with
    """
    target_pokemon = 'raichu'
    egg_groups = pokemon_api_client.get_number_of_egg_groups_by_pokemon_name(target_pokemon)
    expected_egg_groups = 2
    assert egg_groups == expected_egg_groups

def test_smallest_and_biggest_pokemon(pokemon_api_client):
    """
    The function should return a list with the weight of both
    the smallest pokemon and the biggest pokemon i.e. [100, 2]
    """
    weights = pokemon_api_client.get_smallest_and_biggest_pokemon_weight()
    expected_weights_list = [4600, 1]
    assert weights == expected_weights_list
