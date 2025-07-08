# def most_varied(recipes):
#     # Write your solution here!
#     pass

#     # Method 1
#     # chef_ingrediants = {}, key: chef, value: set - list of ingredients

#     # loop through recipes
#         # if chef in chef_ingrediants  up pack
#             # add recipes
#         # if not in chef_ingrediatns
#             # initialize the ditionary, check: recipts

#         # sort the dictoinarys based on the lenght of recipts

#         # return the last two from the last dictoinaries

#     chef_ingrediants = {}

#     for recipe_name, chef, ingredients in recipes:
#         # print(recipe_name)
#         # print(chef)
#         # print(ingredients)

#         if chef in chef_ingrediants:
#             chef_ingrediants[chef].update(set(ingredients))
#         elif chef not in chef_ingrediants:
#             chef_ingrediants[chef] = set()
#             chef_ingrediants[chef].update(set(ingredients))

#     print(chef_ingrediants)

#     sorted_chef_ingrediants = sorted(chef_ingrediants.values(), key=lambda ingredients: len(ingredients))
    
#     print(sorted_chef_ingrediants)

#     # top two ingreditans
#     top_two_ingrediants = []

#     start = -1
#     count = 2
#     while count > 0:
#         sorted_ingredients = sorted(sorted_chef_ingrediants[start])
#         top_two_ingrediants.append(sorted_ingredients)
#         count -= 1
#         start -= 1
    
#     print(top_two_ingrediants)

#     top_1 = set(top_two_ingrediants[0])
#     top_2 = set(top_two_ingrediants[1])

#     result =[None for i in range(2)]
#     # find chef of top two ingrediants
#     for chef, ingrediants in chef_ingrediants.items():
#         if ingrediants == top_1:
#             result[0] = (chef, top_two_ingrediants[0])
#         if ingrediants == top_2:
#             result[1] = (chef, top_two_ingrediants[1])


#     return result 


# # Method 2
# def most_varied(recipes):

#     chef_ingrediants = {}
#     for recipe_name, chef, ingredients in recipes:
#         if chef in chef_ingrediants:
#             chef_ingrediants[chef].update(set(ingredients))
#         elif chef not in chef_ingrediants:
#             chef_ingrediants[chef] = set()
#             chef_ingrediants[chef].update(set(ingredients))

#     print(chef_ingrediants)

#     # sort a dictionary based on the length of its values, descending: reverse=True
#     # sorting a dictionary will give you a new one (usually as a list of tuples 
#     sorted_chef_ingrediants = sorted(chef_ingrediants.items(), key=lambda ingredients: len(ingredients[1]), reverse=True)
    
#     # [
#     #     ('Xinting', {'Carrot', 'Onion', 'Beef', 'Chicken Stock', 'Tomato', 'Peas'}), 
#     #     ('Amy', {'Pepper', 'Tater tots', 'Cheese', 'Chicken Cream'}), 
#     #     ('Sam', {'Tortilla', 'Cheese', 'Beef'}), 
#     #     ('Hallie', {'Oil', 'Potato'})
#     # ]
    
#     print(sorted_chef_ingrediants)

#     # top two ingreditans
#     top_two_ingrediants = []

#     count = 0
#     index = 0

#     while count < 2:
#         chef = sorted_chef_ingrediants[index][0]
#         sorted_ingredients = sorted(sorted_chef_ingrediants[index][1])
#         top_two_ingrediants.append((chef, sorted_ingredients))
#         count += 1
#         index += 1
    
#     print(top_two_ingrediants)


#     return top_two_ingrediants


# Method 3: use .sort
def most_varied(recipes):

    chef_ingrediants = {}
    for recipe_name, chef, ingredients in recipes:
        if chef in chef_ingrediants:
            chef_ingrediants[chef].update(set(ingredients))
        elif chef not in chef_ingrediants:
            chef_ingrediants[chef] = set()
            chef_ingrediants[chef].update(set(ingredients))

    print(chef_ingrediants)

    # sort a dictionary based on the length of its values, descending: reverse=True
    sorted_chef_ingrediants = list(chef_ingrediants.items())
    # print(sorted_chef_ingredients)

    # item is a tuple like ('Alice', {'tomato', 'basil'})
    # item[1] is the set of ingredients → {'tomato', 'basil'}
    sorted_chef_ingrediants.sort(key=lambda item: len(item[1]), reverse=True)
    # print(sorted_chef_ingredients)

    # [
    #     ('Xinting', {'Carrot', 'Onion', 'Beef', 'Chicken Stock', 'Tomato', 'Peas'}), 
    #     ('Amy', {'Pepper', 'Tater tots', 'Cheese', 'Chicken Cream'}), 
    #     ('Sam', {'Tortilla', 'Cheese', 'Beef'}), 
    #     ('Hallie', {'Oil', 'Potato'})
    # ]
    
    print(sorted_chef_ingrediants)

    # top two ingreditans
    top_two_ingrediants = []

    top_1_chef = sorted_chef_ingrediants[0][0]
    top_1_sorted_ingredients = sorted(sorted_chef_ingrediants[0][1])
    top_two_ingrediants.append((top_1_chef, top_1_sorted_ingredients))

    top_2_chef = sorted_chef_ingrediants[1][0]
    top_2_sorted_ingredients = sorted(sorted_chef_ingrediants[1][1])
    top_two_ingrediants.append((top_2_chef, top_2_sorted_ingredients))

    return top_two_ingrediants


recipes_1 = [
    ("Burrito", "Sam", ("Beef", "Cheese", "Tortilla")),
    ("Hot Dish", "Amy", ("Tater tots", "Chicken Cream", "Cheese", "Pepper")),
    ("Stew", "Xinting", ("Beef", "Onion", "Tomato", "Carrot")),
    ("Taco", "Sam", ("Tortilla", "Cheese", "Beef")),
    ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
    ("Latkes", "Hallie", ("Potato", "Oil")),
    ("Pea Soup", "Xinting", ("Peas", "Onion", "Carrot", "Chicken Stock")),
]

print(most_varied(recipes_1))

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