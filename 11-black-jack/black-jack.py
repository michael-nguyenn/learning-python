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

# Displaying Logo
# print(logo)
