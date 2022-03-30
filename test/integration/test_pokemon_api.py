def test_pokemon_name_contains_at_and_double_a(pokemon_api_client):
    """test docs"""
    pokemon_names = pokemon_api_client.get_first_generation_pokemon_names()
    print(pokemon_names)
