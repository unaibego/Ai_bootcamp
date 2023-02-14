class Recipe:
    self.name = 0
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if type(name) != str or name == "":
            print("Name of recipe is wrong")
            return None
        if type(cooking_lvl) != int or cooking_lvl > 5 or cooking_lvl < 1 or cooking_lvl == 0:
            print("Cooking level of recipe is wrong", cooking_lvl)
            return 
        if type(cooking_time) != int or cooking_time <= 0:
            print("Cooking time of recipe is wrong")
            return None
        if type(ingredients) != list or ingredients == []:
            print("Ingredients of recipe are wrong")
            return None
        for string in ingredients:
            if type(string) != str:
              print("Ingredients of recipe are wrong")
              return None
        if type(description) != str:
            print("Description of recipe is wrong")
            return None
        if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert":
            print("Recipe type of recipe is wrong")
            return None
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.name = name
        self.recipe_type = recipe_type
    def __str__(self):
        if self.name:
            print("hola")
        return str(isinstance(self, Recipe))
        # if  isinstance(self, Recipe):
        #     return ("this is the your recipe " +  self.name)
        # else:
        #     return "Bad recipe"
