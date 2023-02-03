recipe = {"ingredients":[], "meal":"", "prep_time":0}
sandwich = recipe
sandwich["ingredients"] = ["ham", "bread", "cheese", "tomatoes"]
sandwich["meal"] = "lunch"
sandwich["prep_time"] = 10
cake = recipe
cake["ingredients"] = ["flour", "sugar", "eggs"]
cake["meal"] = "dessert"
cake["prep_time"] = 60
salad = recipe
salad["ingredients"] = ["avocado", "arugula", "tomatoes", "spinach"]
salad["meal"] = "lunch"
salad["prep_time"] = 15
cookbook = {"sandwich":sandwich, "cake":cake, "salad": salad}
#"indice" bakoitza key deitzen da eta bere balioa value
def print_recipes():
    for recipies in  cookbook.keys():
        print(recipies)

def print_one_recipe(recipe):
    print(cookbook[recipe])

def delete_one_recipe(recipe):
    del cookbook[recipe]

def add_recipe():
    name = input("Enter a name: ")
    print("Enter ingredients: ")
    ingredients = []
    ing = input()
    while (ing != ""):
        ingredients.append(ing)
        ing = input()
    meal = input("Enter meal type: ")
    time = input("Enter a preparation time: ")
    new_recipe = recipe
    new_recipe["ingredients"] = ingredients
    new_recipe["meal"] = meal
    new_recipe["prep_time"] = time
    cookbook[name] = new_recipe
if __name__ == "__main__":
    
    print("Welcome to the Python Cookbook !")
    print("Listo of available option: ")
    print("     1: Add a recipe")
    print("     2: Delete a recipe")
    print("     3: Print a recipe")
    print("     4: Print the cookbook")
    print("     5: Quit")
    while 1:
        print("Please select an option: ")
        i = input(">>")
        if i == "1":
            add_recipe()
        elif i == "2":
            print("Enter a recipie to delete")
            recipe = input(">>")
            if recipe in cookbook:
                delete_one_recipe(recipe)
            else:
                print("Bad input")
        elif i == "3":
            print("Enter a recipie to see")
            recipe = input(">>")
            if recipe in cookbook:
                print_one_recipe(recipe)
            else:
                print("Bad input")
        elif i == "4":
            print_recipes()
        elif i == "5":
            print("Agur guapo")
            break
        else:
            print("Bad input")