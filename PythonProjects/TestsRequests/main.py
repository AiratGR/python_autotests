import requests

HOST = 'https://api.pokemonbattle.ru/v2'
TOKEN = '48ac82da87306091e8f0d2cc7d6859d5'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
BODY_CREATE = {
    "name": "generate",
    "photo_id": -1
}
BODY_CHANGE = {
    "pokemon_id": "43094",
    "name": "Warchitsa",
    "photo_id": 920
}
BODY_TOPOKEBALL = {
    "pokemon_id": "43094"
}

Response_Create = requests.post(url = f'{HOST}/pokemons', headers = HEADER, json = BODY_CREATE)
print(Response_Create.text)

Response_Rename = requests.put(url = f'{HOST}/pokemons', headers = HEADER, json = BODY_CHANGE)
print(Response_Rename.text)

Response_ToPokeball = requests.post(url = f'{HOST}/trainers/add_pokeball', headers = HEADER, json = BODY_TOPOKEBALL)
print(Response_ToPokeball.text)

