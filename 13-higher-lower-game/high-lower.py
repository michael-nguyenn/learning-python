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

print(option_a)
print(option_b)

# Setting up global variables
game_continue = True
guessed_correctly = False
score = 0
temp = ""
while game_continue:
    print(art.logo)
    while guessed_correctly:
        print(f"You're right! Current score: {score}")
        guessed_correctly = False

    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
    print(art.vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")
    usr_choice = input("Who has more followers? Type 'A' or 'B ").upper()

    if (usr_choice == "A" and option_a['follower_count'] > option_b['follower_count']) or usr_choice == "B" and \
            option_b[
                'follower_count'] > option_a['follower_count']:
        score += 1
        guessed_correctly = True
    else:
        guessed_correctly = False

    clear(1)
