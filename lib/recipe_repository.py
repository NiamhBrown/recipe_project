from lib.recipe import Recipe

class RecipeRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from recipes')
        recipes = []
        for row in rows:
            item = Recipe(row["id"],row["name"],row["avg_cooking_time_min"], row["rating"])
            recipes.append(item)
        return recipes
    def find(self, id):
        rows = self._connection.execute('SELECT * from recipes WHERE id = %s', [id])
        row = rows[0]
        return Recipe(row["id"],row["name"],row["avg_cooking_time_min"], row["rating"])
    
    def delete(self,id):
        self._connection.execute('DELETE FROM recipes WHERE id = %s', [id])
        return None
    
    def insert(self, recipe):
        self._connection.execute('INSERT INTO recipes (name, avg_cooking_time_min, rating) VALUES (%s, %s, %s)', [recipe.name, recipe.avg_cooking_time_min, recipe.rating])
        return None
