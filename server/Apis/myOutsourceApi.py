import json
from .api import Api
from Database import dbQueries

class MyOutsourceApi(Api):

    def __init__(self, base_url= ""):
        super().__init__()
        self.url = base_url

    def make_call(self, method = "GET", resources = "", headers = {"Content-Type": "application/json"}):
        self.headers = headers
        self.resources = resources
        self.method = method
        return super().make_call()

    #note, make it more pythonic later
    def proccess_data(self, isGluten=False, isDiary=False):

        recipe_table = [{
            "id": item["idMeal"],
            "title": item["title"],
            "thumbnail": item["thumbnail"],
            "href": item["href"],
            "ingredients": item["ingredients"]
            }
            for item in self.raw_data["results"]]
        final_table = []
        temp_table = []

        if json.loads(isDiary.lower()):
            for recipe in recipe_table:
                take_recipe = True
                for ing in recipe["ingredients"]:
                    if dbQueries.ing_exist("dairy","dairy_ingredients", ing):
                        take_recipe=False
                        break
                if take_recipe:
                    temp_table.append(recipe)
        else:
            temp_table = recipe_table

        if json.loads(isGluten.lower()):
            for recipe in temp_table:
                take_recipe = True
                for ing in recipe["ingredients"]:
                    if dbQueries.ing_exist("gluten","gluten_ingredients", ing):
                        take_recipe=False
                        break
                if take_recipe:
                    final_table.append(recipe)
        else:
            final_table = temp_table

        return {"results": final_table} 