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


def account_format(account):
    """Formats account into - name, description, and country"""
    name = account['name']
    description = account['description']
    country = account["country"]

    return f"{name}, a {description}, from {country}"


def correct_guess(guess, a_followers, b_followers):
    """Returns a boolean value """
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"


def duplicate_checker(account1, account2):
    """Checks if the selections are the same, if so select another account from the dictionary"""
    if account2['name'] == account1['name']:
        account2 = select()
        return account2
    else:
        return account2


def game():
    # Randomly selecting two accounts from the list, and assigning it to option "a", and option "b"
    option_a = select()
    option_b = select()

    duplicate_checker(option_a, option_b)

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

            duplicate_checker(option_a, option_b)

            guessed_correctly = False

        # TESTING CODE
        print(option_a)
        print(option_b)

        print(f"Compare A: {account_format(option_a)}")
        print(art.vs)
        print(f"Against B: {account_format(option_b)}")

        usr_choice = input("Who has more followers? Type 'A' or 'B ").upper()
        a_follower_count = option_a["follower_count"]
        b_follower_count = option_b["follower_count"]

        if correct_guess(usr_choice, a_follower_count, b_follower_count):

            # Saving the account for next comparison
            temp = option_b
            score += 1
            guessed_correctly = True
            clear(1)
        else:
            game_continue = False

    clear(1)
    print(f"Sorry that is not the correct answer :(. Your total score is {score}")


game()
