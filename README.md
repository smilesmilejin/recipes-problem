# recipes-problem
Problem to be completed during Industry Prep - Interview Prep activity time

## Problem Statement

You will be given a data structure containing information on different recipes. It will be a list of tuples, where each tuple represents a single recipe. The tuple will have three elements in this order: the name of the recipe, the name of the chef who created it, and a tuple of ingredients.

For example:

```py
[
    ("Burrito", "Sam", ("Beef", "Cheese", "Tortilla")),
    ("Hot Dish", "Amy", ("Tater tots", "Chicken Cream", "Cheese", "Pepper")),
    ("Stew", "Xinting", ("Beef", "Onion", "Tomato", "Carrot")),
    ("Taco", "Sam", ("Tortilla", "Cheese", "Beef")),
    ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
    ("Latkes", "Hallie", ("Potato", "Oil")),
    ("Pea Soup", "Xinting", ("Peas", "Onion", "Carrot", "Chicken Stock")),
]
```

We are interested in which chefs use the greatest variety of ingredients across all of their recipes. For example, Xinting uses the following ingredients (in alphabetical order):

```py
["Beef", "Carrot", "Chicken Stock", "Onion", "Peas", "Tomato"]
```

This is a larger number of ingredients than any other chef uses. Thus, we will say that Xinting is the most varied chef.

Write a function that takes in a recipes data structure and returns the top two most varied chefs, along with an alphabetically sorted list of the ingredients they each use. This output must be a list of tuples, with the most varied tuple first, and the second most varied second. Each inner tuple will have two elements in this order: the name of the chef, and a sorted list of the unique ingredients they use.

## Examples

### Example 1
```py
recipes_1 = [
    ("Burrito", "Sam", ("Beef", "Cheese", "Tortilla")),
    ("Hot Dish", "Amy", ("Tater tots", "Chicken Cream", "Cheese", "Pepper")),
    ("Stew", "Xinting", ("Beef", "Onion", "Tomato", "Carrot")),
    ("Taco", "Sam", ("Tortilla", "Cheese", "Beef")),
    ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
    ("Latkes", "Hallie", ("Potato", "Oil")),
    ("Pea Soup", "Xinting", ("Peas", "Onion", "Carrot", "Chicken Stock")),
]

most_varied(recipes_1)
```
Produces
```py
[
    ("Xinting", ["Beef", "Carrot", "Chicken Stock", "Onion", "Peas", "Tomato"]), 
    ("Amy", ["Cheese", "Chicken Cream", "Pepper", "Tater tots"])
]
```

### Example 2
```py
recipes_2 = [
    ("Latkes", "Hallie", ("Potato", "Oil")),
    ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
]

most_varied(recipes_2)
```
Produces
```py
[("Sam", ["Beef", "Cheese", "Tortilla"]), ("Hallie", ["Oil", "Potato"])]
```

## Notes for the Interviewer

### Clarifying Questions

#### Q: How should I handle invalid input?
A: You can assume the input will be valid.

#### Q: How should I handle empty input? Or input with only one chef?
A: You can assume the input will be non-empty and have at least two chefs.

#### Q: Does capitalization matter?
A: Yes.

### Hints

- If your candidate is struggling to form an algorithm, encourage them to explain how they would do it by hand. Afterwards help them to see what data structures might be useful.

- If your candidate is struggling with a subpart of the problem (e.g. sorting or getting the top 2), encourage them to first focus on writing a solution to a simpler version of the problem that does not include those requirements.

- If your candidate is struggling to get unique elements, ask them what data structure (sets) could help them there.
