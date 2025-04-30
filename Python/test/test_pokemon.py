import requests
import pytest

URL = 'https://pokemonbattle.ru/v2'
TOKEN = 'd1a26db33643d6746bf4c0f5a8a54c16'
HEADER = {'Content-Type': 'application/json'}
TRAINER_ID = '30330'

def test_get_trainers():
   response = requests.get(url=f'{URL}/trainers', headers=HEADER, params = {'treiner_id':TRAINER_ID})
   assert response.status_code == 200

def test_get_treiner_id():
   response_get = requests.get(url=f'{URL}/trainers', headers=HEADER, params = {'treiner_id':TRAINER_ID})
   assert response_get.json()[0]['name'] == 'FOX'