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
names = names_string.split(", ")  # This removes the comma and the space from our input

# Calculating the index of our list
index = random.randint(0, len(names) - 1)

print(f"{names[index]} is going to buy the meal today!")


# TREASURE MAP
# Marking a spot with an x. Input is 2 digits coordinates that will correspond to a grid of 9, created
# with nested lists

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]

map = [row1, row2, row3]

# position = input("Where do you want to put the treasure? ")
position = 23

# Converting user input to usable format
index_coordinates = list(str(position))
row_index = int(index_coordinates[1]) - 1
column_index = int(index_coordinates[0]) - 1


map[row_index][column_index] = "X"
print(f"{row1}\n{row2}\n{row3}")