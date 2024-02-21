import json
import requests

def example(a):
    #a = 45
    base_url = 'https://dummyjson.com/recipes?limit=' + str(a)
    get_JSON=requests.get(base_url)
    JSON_data=get_JSON.json()

    for i in range(a):
        id = JSON_data["recipes"][i]['id']
        n = JSON_data["recipes"][i]['name']
        ingr = JSON_data["recipes"][i]['ingredients']
        instr = JSON_data["recipes"][i]['instructions']

        print('id: ', id)
        print('name: ', n)
        print('ingredients: ', ingr)
        print('instructions: ', instr)

example(45)