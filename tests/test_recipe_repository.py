from lib.recipe import Recipe
from lib.recipe_repository import RecipeRepository

# we want to test all, find, insert and delete

def test_gets_all_recipes(db_connection):
    db_connection.seed("seeds/recipe.sql")
    repository = RecipeRepository(db_connection)

    recipes = repository.all()

    assert recipes == [
    Recipe(1,'pizza', 30, 5),
    Recipe(2,'spagetti', 35, 4),
    Recipe(3,'toast', 5, 2),
    Recipe(4,'noodles', 20, 5),
    Recipe(5,'soup', 45, 3),
    ]

def test_return_recipe_with_id(db_connection):
    db_connection.seed("seeds/recipe.sql")
    repository = RecipeRepository(db_connection)

    recipe = repository.find(1)

    assert recipe == Recipe(1,'pizza', 30, 5)

def test_delete(db_connection):
    db_connection.seed("seeds/recipe.sql")
    repository = RecipeRepository(db_connection)
    repository.delete(1)
    result = repository.all()

    assert result == [    
    Recipe(2,'spagetti', 35, 4),
    Recipe(3,'toast', 5, 2),
    Recipe(4,'noodles', 20, 5),
    Recipe(5,'soup', 45, 3)]

def test_insert(db_connection):
    db_connection.seed("seeds/recipe.sql")
    repository = RecipeRepository(db_connection)

    repository.insert(Recipe(None, 'tomato pasta', 20, 4))
    result = repository.all()
    assert result == [
    Recipe(1,'pizza', 30, 5),
    Recipe(2,'spagetti', 35, 4),
    Recipe(3,'toast', 5, 2),
    Recipe(4,'noodles', 20, 5),
    Recipe(5,'soup', 45, 3),
    Recipe(6, 'tomato pasta', 20, 4)
    ]