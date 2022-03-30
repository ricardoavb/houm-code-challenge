from commons.pokemon_api_client import PokemonApiClient
import pytest


@pytest.fixture
def pokemon_api_client():
    return PokemonApiClient()
