import pytest

@pytest.mark.skip
def test_get_pokemon_type_by_name(pokemon_api_client):
    pokemon_name = 'kakuna'
    types_list = pokemon_api_client.get_pokemon_type_by_name(pokemon_name)
    expected_types_list = ['bug', 'poison']
    assert types_list == expected_types_list

@pytest.mark.skip
def test_get_all_pokemon(pokemon_api_client):
    """
    The function should return the total number of pokemon (all generations)
    """
    expected_pokemon_count = 1126
    pokemon_count = len(pokemon_api_client.get_all_pokemon_names())
    assert pokemon_count == expected_pokemon_count


@pytest.mark.skip
def test_pokemon_name_contains_at_and_double_a(pokemon_api_client):
    """
    The function should return the number of occurrences a list of pokemon names contains
    both, twice 'a' and 'at', i.e. 'raticate'
    """
    matches = pokemon_api_client.get_filtered_first_generation_pokemon_names_matches()
    expected_matches = 1
    assert matches == expected_matches


@pytest.mark.skip
def test_raichu_compatible_species(pokemon_api_client):
    """
    The function should return the number of species (egg groups)
    a given pokemon is compatible with
    """
    target_pokemon = 'raichu'
    egg_groups = pokemon_api_client.get_number_of_egg_groups_by_pokemon_name(
        target_pokemon)
    expected_egg_groups = 2
    assert egg_groups == expected_egg_groups

#@pytest.mark.skip
def test_biggest_and_smallest_fighting_pokemon_weight(pokemon_api_client):
    """
    The function should return a list with the weight of both,
    the biggest pokemon and the smallest pokemon i.e. [1300, 195]
    """
    weights = pokemon_api_client.get_biggest_and_smallest_pokemon_weight(pokemon_type='fighting')
    expected_weights_list = [1300, 195]
    assert weights == expected_weights_list
