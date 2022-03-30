"""
    Pokemon API test suite
"""

def test_pokemon_name_contains_at_and_double_a(pokemon_api_client):
    """
    The function should return the number of occurrences a list of pokemon names contains
    both, twice 'a' and 'at', i.e 'raticate' 
    """
    matches = pokemon_api_client.get_filtered_first_generation_pokemon_names_matches()
    expected_matches = 1
    assert matches == expected_matches
