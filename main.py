def most_varied(recipes):
    # Create a dictionary of chefs to a set of ingredients they use
    # For example {"Sam": {"Tortilla", "Beef", "Cheese"}}
    unique_ingredients = {}
    #Iterate over the recipes, unpacking the needed values
    for _, chef, ingredients in recipes:
        # If this is the first time we have seen this chef
        if chef not in unique_ingredients:
            # Start with all the ingredients for the first recipe
            unique_ingredients[chef] = set(ingredients)
        else:
            # Add each ingredient from the new recipe
            # The set avoids creating duplicates
            for ingredient in ingredients:
                unique_ingredients[chef].add(ingredient)
    
    # Create a list of tuples. where each tuple contains
    # the number of unique ingredients used, then the chef
    # For example: [(2, "Hallie"), (3, "Sam")]
    counts = []
    for chef, ingredients in unique_ingredients.items():
        counts.append((len(ingredients), chef))

    # Sort the counts in descending order and select the top 2
    counts.sort(reverse=True)
    top_two = counts[:2]

    # Convert the data into the final result
    result = []
    for _, chef in top_two:
        sorted_ingredients = sorted(list(unique_ingredients[chef]))
        result.append((chef, sorted_ingredients))

    return result


recipes_1 = [
    ("Burrito", "Sam", ("Beef", "Cheese", "Tortilla")),
    ("Hot Dish", "Amy", ("Tater tots", "Chicken Cream", "Cheese", "Pepper")),
    ("Stew", "Xinting", ("Beef", "Onion", "Tomato", "Carrot")),
    ("Taco", "Sam", ("Tortilla", "Cheese", "Beef")),
    ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
    ("Latkes", "Hallie", ("Potato", "Oil")),
    ("Pea Soup", "Xinting", ("Peas", "Onion", "Carrot", "Chicken Stock")),
]
assert most_varied(recipes_1) == [
    ("Xinting", ["Beef", "Carrot", "Chicken Stock", "Onion", "Peas", "Tomato"]), 
    ("Amy", ["Cheese", "Chicken Cream", "Pepper", "Tater tots"])
]

recipes_2 = [
    ("Latkes", "Hallie", ("Potato", "Oil")),
    ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
]
assert most_varied(recipes_2) == [
    ("Sam", ["Beef", "Cheese", "Tortilla"]),
    ("Hallie", ["Oil", "Potato"])
]

print("All test cases passed!")
print("Finished early? Discuss time & space complexity.")