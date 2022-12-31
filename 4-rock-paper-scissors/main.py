# Python uses the Mersenne Twister - a pseudorandom generator

# Importing Custom Module
import module

# Importing the random module
import random

# Importing a specific thing from a module as well
# from random import randint

random_integer = random.randint(1, 10)
# random_integer = randint(1, 10)
print(random_integer)

print(module.pi)

# Using from random module
random_float = random.random()  # Returns a float from 0-0.99

# Using random() to generate a number between 0-5, no including 5
print(round(random_float * 5, 1))


# Lists aka Arrays

# Lists are ordered, via index, and can store any data type, just like JS

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"]

first_state = states_of_america[0]  # "Delaware"
last_state = states_of_america[-1]  # "Connecticut

states_of_america[1] = "Pencilvania"

# append() add an item to the end of the list
states_of_america.append("Michael-Land")

# extend() adds a list to the end of the list
states_of_america.extend(["Irene", "Henry"])

print(states_of_america)

# .split() is a string method that returns a list of the words in the string, separated by the
# # delimiter string


# IndexErrors & Working with Nested Lists

# IndexOutOfRangeException - Accessing an index where a list element doesn't exist

# Nested Lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)