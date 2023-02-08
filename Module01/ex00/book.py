from datetime import date
class Book:
    recipes_list = {"starter":[], "lunch":[], "dessert":[]}
    def __init__(self, name):
        if type(name) != str or name == "":
            print("Name of recipe is wrong")
            quit()
        self.name = name
        self.creation_date = date.today()
        self.last_update = date.today()
    def get_recipe_by_name(self, name):
        for lista in list(self.recipes_list.values()):
            for recipe in lista:
                if recipe.name == name:
                    print(recipe)
                    return 0
        print("There are no recipes with that name")
    def add_recipe(self, recipe):
            self.recipes_list[recipe.recipe_type].append(recipe)



