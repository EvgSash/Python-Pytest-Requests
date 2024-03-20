import requests

URL = 'https://api.pokemonbattle.me/v2/'
TOKEN = '989c3e9f8b0615c610b98693487d1502'
ID = '2371'
trainer_id = '371'
HEADERS = {
    'Content-Type' : 'application/json',
    'trainer_token': TOKEN
    }

body_add_pokemon = {
    "name": "generate",
    "photo": "generate"
}

body_rename_pokemon = {
    "pokemon_id": ID,
    "name": "pytest",
    "photo": "https://dolnikov.ru/pokemons/albums/099.png"
}

body_catch_pokemon = {
    "pokemon_id": ID
}

add_pokemon = requests.post(url = f'{URL}pokemons', headers = HEADERS, json = body_add_pokemon)                         # создать покемона

print(add_pokemon.text)

rename_pokemon = requests.put(url = f'{URL}pokemons', headers = HEADERS, json = body_rename_pokemon)                    # изменить покемона

print(rename_pokemon.text)

catch_pokemon = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADERS, json = body_catch_pokemon)        # поймать покемона

print(catch_pokemon.text)

