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
        print(i)
        if hand[i] == 11 and sum(hand) > 21:
            hand[i] = 1


# Drawing a Card
def draw_card():
    return random.choice(cards)


# Calculating Score
def calculate_score(hand):
    return sum(hand)


# Calculating Black Jack
def black_jack(score, user):
    if score == 21:
        print(f"Black Jack! {user} wins.")
        sys.exit()


# Displaying Logo
print(logo)

continue_game = True

while continue_game:
    # User and Computer Hands
    user_hand = []
    computer_hand = []

    # Randomly Assigning 2 cards each
    for _ in range(2):
        user_hand.append(draw_card())
        computer_hand.append(draw_card())

    # print(f"User Hand: {user_hand}\nComputer Hand: {computer_hand}")

    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)

    # Order matters, because if both players have blackjack, computer will win
    black_jack(computer_score, "Computer")

    black_jack(user_score, "User")

    if user_score == 21:
        print(f"BlackJack {user_hand}! You win~")
        time.sleep(1)
        # print("Would you like to play again?")

    # Showing Computer's First Card
    print(f"Computer's Hand: [{computer_hand[0]}, _ ]")

    # Setting up Continue Condition for User
    user_continue = True

    while user_continue and user_score < 21:

        print(f"Your Hand: {user_hand}")
        user_decision = input("Press 'y' to draw another card, or 'n' to end your turn: ".lower())

        if user_decision == 'n':
            user_continue = False
        else:
            user_hand.append(draw_card())
            user_score = calculate_score(user_hand)

            black_jack(user_score, "User")

            if user_score > 21:
                clear()
                print(f"{user_hand}. You lose!")
                sys.exit()

    while computer_score <= 16:
        computer_hand.append(draw_card())
        computer_score = (calculate_score(computer_hand))

        black_jack(computer_score, "Computer")

        if computer_score > 21:
            clear()
            print(f"{computer_hand}. You win!")
            sys.exit()

    clear()
    print(f"Your Hand: {user_hand} and Score: {user_score}\nComp's Hand: {computer_hand} and Score: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You win~")
    elif computer_score == user_score:
        print("It's a tie!")
    else:
        print("Sorry you lost.")

    play_again = input("Press 'y' to play again or 'no' to quit the program ")

    if play_again == 'n':
        continue_game = False

    clear()
