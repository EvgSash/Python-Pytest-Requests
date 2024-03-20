import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2/'
TOKEN = '989c3e9f8b0615c610b98693487d1502'
HEADERS = {
    'Content-Type' : 'application/json',
    'trainer_token': TOKEN
    }
trainer_id = '371'

def test_status_code():
    trainers = requests.get(url = f'{URL}trainers', headers = HEADERS, params = f'trainer_id={trainer_id}')
    assert trainers.status_code == 200

def test_part_of_response():
    trainers = requests.get(url = f'{URL}trainers', headers = HEADERS, params = f'trainer_id={trainer_id}')
    assert trainers.json()['data'][0]['trainer_name'] == "Alucard"

