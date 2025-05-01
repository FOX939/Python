import requests

URL = "https://pokemonbattle.me:9104"
TOKEN = "d2a1d2b3a3b34a0b7acf6f3a5ac8a5ac"
HEADER = {"Content-Type": "application/json"}

body_registration = {
    "trainer": "Anatol",
    "photo_id": 1
}

body_newname = {
    "pokemon_id": "725714",
    "name": "Braeden",
    "photo_id": 5
}

body_catchpokemon = {
    "pokemon_id": "725714"
}

response = requests.post(f"{URL}/pokemons", headers=HEADER, json=body_registration)
print(response.json())

response = requests.put(f"{URL}/pokemons", headers=HEADER, json=body_newname)
print(response.json())

response = requests.post(f"{URL}/trainers/add_pokeball", headers=HEADER, json=body_catchpokemon)
print(response.json())
