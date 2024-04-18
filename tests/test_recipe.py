from lib.recipe import Recipe

def test_recipe_constructs():
    recipe = Recipe(1, 'sandwich', 5, 4)
    assert recipe.id == 1
    assert recipe.name == 'sandwich'
    assert recipe.avg_cooking_time_min == 5
    assert recipe.rating == 4

def test_recipe_format():
    recipe = Recipe(1, 'sandwich', 5, 4)
    assert str(recipe) == "Recipe(1, sandwich, 5, 4)"

def test_equal_recipe():
    recipe1 = Recipe(1, 'sandwich', 5, 4)
    recipe2 = Recipe(1, 'sandwich', 5, 4)
    assert recipe1 == recipe2