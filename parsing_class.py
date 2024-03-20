import json
import requests

class Recipes:
    def __init__(self, a, base_url):
        self.a = a
        self.base_url = base_url
        self.id = id
        #self.name = name

    def get_ID(self, a):
        base_url = 'https://dummyjson.com/recipes?limit=' + str(a)
        get_JSON = requests.get(base_url)
        JSON_data = get_JSON.json()
        for i in range(a):
            id = JSON_data["recipes"][i]['id']
            print('id: ', id)
        return id

    def get_Name(self, a):
        base_url = 'https://dummyjson.com/recipes?limit=' + str(a)
        get_JSON = requests.get(base_url)
        JSON_data = get_JSON.json()
        for i in range(a):
            name = JSON_data["recipes"][i]['name']
            print('name: ', name)
        return name

            #print('name: ', n)
            #print('ingredients: ', ingr)
            #print('instructions: ', instr)"""

obj = Recipes(5, 'https://dummyjson.com/recipes?limit=' + str(10))

obj.get_ID(11)

#obj.get_Name(5)