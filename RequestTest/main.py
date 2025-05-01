import requests

URL = 'https://pokemonbattle.ru/v2'
TOKEN = 'd1a26db33643d6746bf4c0f5a8a54c16'
HEADER = {'Content-Type': 'application/json'}
body_registration={
    "name": "Аватвр",
    "photo_id": -1
}
body_newname = {
    "pokemon_id": "225714",
    "name": "Braeden",
    "photo_id": 5
}

body_cachpokemon = {
    "pokemon_id": "225714"
}
requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_registration)
print(requests.json()['data'])

requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_newname)
print(requests.json()['data'])

requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_cachpokemon)
print(requests.json()['data'])




