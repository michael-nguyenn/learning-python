import random

# HEAD OR TAILS GENERATOR #######

# Generates a float between 0-0.99
random_value = round(random.random())

if random_value == 1:
    print("Heads")
else:
    print("Tails")

# BANKER ROULETTE
# A program that will select a random name from a list of names. The person selected will have to pay for
# everybody's food bill


names_string = "Michael, Irene, Henry, Claire, Desmond, Dina, Victor"

# .split() our string into an array
names = names_string.split(", ")

# Calculating the index of our list
index = random.randint(0, len(names) - 1)

print(f"{names[index]} is going to buy the meal today!")

