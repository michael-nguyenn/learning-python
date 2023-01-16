# Number Guessing Game

# Computer Generates a number from 1-100
# User Chooses a difficulty level either easy or hard
#   This will determine how many lives the user gets: either 10 or 5
# User Starts guessing
#   If their guess is too high -> print to console too high
#   if their guess is too low -> print to console their guess is too low
#   if they get it then they get it!


import art
from random import randint
from time import sleep


def wait(time):
    """Simulating Waiting"""
    sleep(time)


# Start and Introduction to game
print(art.logo)
print("Hello and Welcome! Can you guess my number?!")

# Generating a number from 1-100
magic_number = randint(1, 100)

# We don't actually have to create the variable lives right here, but we are appeasing the python gods
# who state lives may not be defined
lives = 0

# Setting up a boolean to make sure a valid input is in place
valid_response = False

while not valid_response:
    user_difficulty = input("Choose a difficulty. Type 'ez' or 'hard': ").lower()

    if user_difficulty == "ez":
        lives = 10
        valid_response = True
    elif user_difficulty == "hard":
        lives = 5
        valid_response = True
    else:
        print("Please put a valid response....")
        wait(1)

game_over = False

while not game_over:
    guess = int(input("Please make a guess: "))

    if guess > magic_number:
        print("Too High")
        lives -= 1
    elif guess < magic_number:
        print("Too Low")
        lives -= 1
    else:
        print(art.win_msg)
        print("You guessed it!")
        game_over = True
        break

    if lives == 0:
        print("You ran out of lives homie.")
        wait(1)
        print("Game Over")
        break

    print("Guess again~")
    wait(1)
