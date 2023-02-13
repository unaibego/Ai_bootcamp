from recipe import Recipe
from book import Book

# tortita = Recipe("tortita", 8, 5, ["jejejee", "jajaja"], "Hola",  recipe_type="lunch")
txokolate = Recipe("txokolat", 3, 5, ["jejejee", "jajaja"], "Hola",  recipe_type="lunch")
libro = Book("Libro")
# libro.add_recipe(tortita)
libro.add_recipe(txokolate)
libro.get_recipe_by_name("txokolat")
