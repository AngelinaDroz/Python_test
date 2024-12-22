from typing import Literal
import requests
import pytest 

URL = 'https://api.pokemonbattle.ru/v2' 
TOKEN = 'df18d718f19784d9051fec89b2c94523'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '12312'
TRAINER__NAME = 'Slipnkot'
LEVEL = '4'


def test_status_code(): 
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID}) 
    assert response.status_code == 200
    
def test_part_of_response(): 
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID}) 
    assert response_get.json()["data"][0]["name"] == 'Tekila'
    
    
@pytest.mark.parametrize('key, value', [('name', 'Tekila'),('trainer_id', TRAINER_ID),('id', '165893')])
def test_parametrize(key: Literal['name'] | Literal['trainer_id'] | Literal['id'], value: Literal['Tekila'] | Literal['12312'] | Literal['165893']): 
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID}) 
    assert response_parametrize.json()["data"][0][key] == value
    
def test_name(): 
    response_get = requests.get(url = f'{URL}/me', headers = HEADER, params = TRAINER_ID)    
    assert response_get.json()["data"][0]["trainer_name"] == 'Slipknot'