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
