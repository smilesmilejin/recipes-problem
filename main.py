def most_varied(recipes):
    # Write your solution here!
    pass

    # Method 1
    # chef_ingrediants = {}, key: chef, value: set - list of ingredients

    # loop through recipes
        # if chef in chef_ingrediants  up pack
            # add recipes
        # if not in chef_ingrediatns
            # initialize the ditionary, check: recipts

        # sort the dictoinarys based on the lenght of recipts

        # return the last two from the last dictoinaries

    chef_ingrediants = {}

    for recipe_name, chef, ingredients in recipes:
        # print(recipe_name)
        # print(chef)
        # print(ingredients)

        if chef in chef_ingrediants:
            chef_ingrediants[chef].update(set(ingredients))
        elif chef not in chef_ingrediants:
            chef_ingrediants[chef] = set()
            chef_ingrediants[chef].update(set(ingredients))

    print(chef_ingrediants)

    sorted_chef_ingrediants = sorted(chef_ingrediants.values(), key=lambda ingredients: len(ingredients))
    
    print(sorted_chef_ingrediants)

    # top two ingreditans
    top_two_ingrediants = []

    start = -1
    count = 2
    while count > 0:
        sorted_ingredients = sorted(sorted_chef_ingrediants[start])
        top_two_ingrediants.append(sorted_ingredients)
        count -= 1
        start -= 1
    
    print(top_two_ingrediants)

    top_1 = set(top_two_ingrediants[0])
    top_2 = set(top_two_ingrediants[1])

    result =[None for i in range(2)]
    # find chef of top two ingrediants
    for chef, ingrediants in chef_ingrediants.items():
        if ingrediants == top_1:
            result[0] = (chef, top_two_ingrediants[0])
        if ingrediants == top_2:
            result[1] = (chef, top_two_ingrediants[1])


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

# print(most_varied(recipes_1))

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