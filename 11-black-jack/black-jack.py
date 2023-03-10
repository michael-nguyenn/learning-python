# Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# Jack/Queen/King all count as 10.
# Ace can count as 11 or 1.
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import os
import time
import random
from art import logo
import sys


# Creating a clear function to clear the console
def clear(seconds=0):
    time.sleep(seconds)
    os.system('clear')


# Deck of Cards Used
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Ace Checker
def ace_checker(hand):
    for i in range(len(hand)):
        if hand[i] == 11 and sum(hand) > 21:
            hand[i] = 1


# Deal Card Function
def deal_cards(hand, amount):
    """Input the hand, and how many cards you want to draw"""
    for _ in range(amount):
        hand.append(random.choice(cards))


# Calculating Score
def calculate_score(hand):
    # Checking for BlackJack - One Ace and One Face Card
    if len(hand) == 2 and sum(hand) == 21:
        return 0

    # Calling Ace Checker
    ace_checker(hand)

    return sum(hand)


# Comparing Scores Function
def compare(usr_score, comp_score):
    if usr_score > comp_score or comp_score > 21:
        print("You win")
    elif usr_score == comp_score:
        print("It's a tie")
    else:
        print("You lose")


# Simulating Time
def wait(seconds):
    time.sleep(seconds)


# Displaying Logo
print(logo)

continue_game = True

while continue_game:
    # User and Computer Hands
    user_hand = []
    computer_hand = []

    # Drawing Two Cards Each to Start the game
    deal_cards(user_hand, 2)
    deal_cards(computer_hand, 2)

    computer_score = calculate_score(computer_hand)
    user_score = calculate_score(user_hand)

    # Showing Computer's First Card
    print(f"Computer's Hand: [{computer_hand[0]}, _ ]")

    # Setting up Continue Condition for User
    user_continue = True
    game_over = False

    while user_continue:

        print(f"Your Hand: {user_hand}, Your Score: {user_score}")

        if computer_score == 0 or user_score > 21:
            print("-----------------------")
            wait(1)
            print(f"Computer's Hand: {computer_hand}")
            print("Womp Womp... You lose!")
            game_over = True
            break

        if user_score == 0:
            print("-----------------------")
            print("Black Jack!!! You win!")
            game_over = True
            break

        user_decision = input("Press 'y' to draw another card, or 'n' to end your turn: ".lower())

        if user_decision == 'n':
            user_continue = False
        else:
            deal_cards(user_hand, 1)
            user_score = calculate_score(user_hand)

            calculate_score(user_hand)

    if not game_over:
        print("Computer's turn.......")

        while computer_score < 17:
            wait(1)
            deal_cards(computer_hand, 1)
            print(f"Computer draws a {computer_hand[-1]}")
            computer_score = calculate_score(computer_hand)

        print("Final Score.....")
        wait(1)
        print(f"Your Hand: {user_hand}, Your Score: {user_score}")
        print(f"Computer Hand: {computer_hand}, Computer Score: {computer_score}")
        compare(user_score, computer_score)

    play_again = input("Press 'y' to play again or 'n' to quit the program ")

    clear(1)

    if play_again == 'n':
        continue_game = False
