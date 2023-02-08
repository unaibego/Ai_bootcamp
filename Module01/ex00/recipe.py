class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if type(name) != str or name == "":
            print("Name of recipe is wrong")
            quit()
        self.name = name
        if type(cooking_lvl) != int or cooking_lvl > 5 or cooking_lvl < 1 or cooking_lvl == 0:
            print("Cooking level of recipe is wrong")
            quit()
        self.cooking_lvl = cooking_lvl
        if type(cooking_time) != int or cooking_time <= 0:
            print("Cooking time of recipe is wrong")
            quit()
        self.cooking_time = cooking_time
        if type(ingredients) != list or ingredients == []:
            print("Ingredients of recipe are wrong")
            quit()
        for string in ingredients:
            if type(string) != str:
              print("Ingredients of recipe are wrong")
              quit()
        self.ingredients = ingredients
        if type(description) != str:
            print("Description of recipe is wrong")
            quit()
        self.description = description
        if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert":
            print("Recipe type of recipe is wrong")
            quit()
        self.recipe_type = recipe_type
    def __str__(self):
        return ("this is the your recipe " +  self.name)

    