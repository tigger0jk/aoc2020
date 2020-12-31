import re

allergensToPossibleIngredients = {}
ingredientsToPossibleAllergens = {}
ingredientCounts = {}
f = open("input.txt", "r")
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    # mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
    # trh fvjkl sbzzf mxmxvkd (contains dairy)
    res = re.search("([\w ]*) \(contains ([\w ,]*)\)", strippedLine)
    ingredients = set(res.group(1).split(' '))
    print(ingredients)
    allergens = set(res.group(2).split(', '))
    print(allergens)
    for allergen in allergens:
        if allergen not in allergensToPossibleIngredients:
            allergensToPossibleIngredients[allergen] = ingredients
        else:
            allergensToPossibleIngredients[allergen] = ingredients.intersection(allergensToPossibleIngredients[allergen])

    for ingredient in ingredients:
        if ingredient not in ingredientCounts:
            ingredientCounts[ingredient] = 1
        else:
            ingredientCounts[ingredient] = ingredientCounts[ingredient] + 1

print(allergensToPossibleIngredients)
for allergen, ingredients in allergensToPossibleIngredients.items():
    for ingredient in ingredients:
        if ingredient not in ingredientsToPossibleAllergens:
            ingredientsToPossibleAllergens[ingredient] = set([allergen])
        else:
            ingredientsToPossibleAllergens[ingredient] = set([allergen]).union(ingredientsToPossibleAllergens[ingredient])

print(ingredientsToPossibleAllergens)
zeroAllergenIngredients = set()

print(ingredientCounts)
totalCount = 0
for ingredient, count in ingredientCounts.items():
    if ingredient not in ingredientsToPossibleAllergens:
        totalCount = totalCount + count

print(totalCount)
