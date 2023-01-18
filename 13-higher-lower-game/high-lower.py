# Higher Lower Game...
# Game is designed to give the user a choice between two persons from a list, and choose who has more followers.
# If chosen correctly, you continue on until you lose, then we give the score

# From the dictionary, randomly select a person from the list, and assign it to A, and B
#   ?Create a function to random retrieve a person

# Then ask user to choose who has more followers
#   If they guess correctly, the correct answer becomes option A
#   Randomly select a person from the list and assign to person B
#   Tally the person's correct guesses

#   If they guess wrong, then the game ends, we let the user know how many correct guesses they had


import art
import random
from game_data import data
import time
import os


def select():
    """Randomly selects a person from the list"""
    return random.choice(data)


def clear(seconds=0):
    time.sleep(seconds)
    os.system('clear')


# Randomly selecting two accounts from the list, and assigning it to option "a", and option "b"
option_a = select()
option_b = select()

# Setting up global variables
game_continue = True
guessed_correctly = False
score = 0
temp = {}

while game_continue:
    print(art.logo)

    # If user picked correct option
    while guessed_correctly:
        print(f"You're right! Current score: {score}")

        # Assign the correct guess to option A, and generate a new option B
        option_a = temp
        option_b = select()

        if option_b['name'] == option_a['name']:
            option_b = select()

        guessed_correctly = False

    print(option_a)
    print(option_b)

    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
    print(art.vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")
    usr_choice = input("Who has more followers? Type 'A' or 'B ").upper()

    if (usr_choice == "A" and int(option_a['follower_count']) > int(
            option_b['follower_count'])) or usr_choice == "B" and \
            int(option_b[
                    'follower_count']) > int(option_a['follower_count']):

        # Saving the account for next comparison
        if usr_choice == "A":
            temp = option_a
        else:
            temp = option_b

        score += 1
        guessed_correctly = True
        clear(1)
    else:
        game_continue = False

clear(1)
print(f"Sorry that is not the correct answer :(. Your total score is {score}")
