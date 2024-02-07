import json
import requests

base_url = 'https://dummyjson.com/recipes'
get_JSON=requests.get(base_url)
JSON_data=get_JSON.json()

for i in range(30):
    ID=JSON_data["recipes"][i]['id']
    N=JSON_data["recipes"][i]['name']
    Ingr=JSON_data["recipes"][i]['ingredients']

    print('id: ', ID)
    print('name: ', N)
    print('ingredients: ', Ingr)