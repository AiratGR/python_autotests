import requests
import pytest

HOST = 'https://api.pokemonbattle.ru/v2'
TOKEN = '48ac82da87306091e8f0d2cc7d6859d5'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
QUERY = {'trainer_id' : '4267'}

def test_status_code():
    response = requests.get(url = f'{HOST}/trainers', params = QUERY)
    assert response.status_code == 200

def test_say_my_name():
    r = requests.get(url = f'{HOST}/trainers', params = QUERY)
    assert r.json()['data'][0]['trainer_name'] == 'Airat'