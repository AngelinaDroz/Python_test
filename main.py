import requests

URL = 'https://api.pokemonbattle.ru/v2' 
TOKEN = 'df18d718f19784d9051fec89b2c94523'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Vodka",
    "photo_id": 98
}

body_add_pokeball = {
    "pokemon_id": "166522"
}

body_new_name = {
    "pokemon_id": "166523",
    "name": "Viski",
    "photo_id": 98
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''message = response_create.json()['message']
print(message)'''

'''response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)'''

response_change_name_pok = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_new_name)
print(response_change_name_pok.text)