import random

# HEAD OR TAILS GENERATOR #######

# Generates a float between 0-0.99
random_value = round(random.random())

if random_value == 1:
    print("Heads")
else:
    print("Tails")
