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

    def proccess_data(self, isDiary=False, isLectose=False):
        
        # recipe_table = [{
        #     "idMeal": item["idMeal"],
        #     "title": item["title"],
        #     "strDrinkAlternate": item["strDrinkAlternate"],
        #     "strCategory": item["strCategory"],
        #     "strArea": item["strArea"],
        #     "strInstructions": item["strInstructions"],
        #     "thumbnail": item["thumbnail"],
        #     "strTags": item["strTags"],
        #     "href": item["href"],
        #     "ingredients": item["ingredients"]
        #     }
        #     for item in self.raw_data["results"]]

        recipe_table = [{
            "title": item["title"],
            "thumbnail": item["thumbnail"],
            "href": item["href"],
            "ingredients": item["ingredients"]
            }
            for item in self.raw_data["results"]]
        
        for item in recipe_table:
                print("added")

        # dbQueries.get_table("gluten")

        return self.raw_data
