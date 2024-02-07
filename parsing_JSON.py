import json
import requests

a = 45

base_url = 'https://dummyjson.com/recipes?limit=' + str(a)
get_JSON=requests.get(base_url)
JSON_data=get_JSON.json()

for i in range(a):
    ID=JSON_data["recipes"][i]['id']
    N=JSON_data["recipes"][i]['name']
    Ingr=JSON_data["recipes"][i]['ingredients']

    print('id: ', ID)
    print('name: ', N)
    print('ingredients: ', Ingr)