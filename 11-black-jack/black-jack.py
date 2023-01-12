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


# Displaying Logo
# print(logo)


# User and Computer Hands
user_hand = []
computer_hand = []

# Randomly Assigning 2 cards each
for _ in range(2):
    user_hand.append(random.choice(cards))
    computer_hand.append(random.choice(cards))

print(f"User Hand:{user_hand}\nComputer Hand:{computer_hand}")

# Order matters, because if both players have blackjack, computer will win
if sum(computer_hand) == 21:
    print(f"Computer got black jack {computer_hand}! You lose...")
    time.sleep(1)
    # print("Would you like to play again?")

if sum(user_hand) == 21:
    print(f"BlackJack {user_hand}! You win~")
    time.sleep(1)
    # print("Would you like to play again?")
