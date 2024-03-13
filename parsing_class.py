import json
import requests

class Recipes:
    def __init__(self):
        self.a = a
        self.base_url = 'https://dummyjson.com/recipes?limit=' + str(a)

    def get_ID(a):
        # a = 45
        get_JSON = requests.get(self.base_url)
        JSON_data = get_JSON.json()
        for i in range(a):
            id = JSON_data["recipes"][i]['id']
        return id

        """for i in range(a):
            id = JSON_data["recipes"][i]['id']
            n = JSON_data["recipes"][i]['name']
            ingr = JSON_data["recipes"][i]['ingredients']
            instr = JSON_data["recipes"][i]['instructions']"""

        print('id: ', id)
            #print('name: ', n)
            #print('ingredients: ', ingr)
            #print('instructions: ', instr)"""

obj = Recipes()

obj.get_ID()