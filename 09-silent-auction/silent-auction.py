import os
import time
from art import logo


# Creating a clear function to clear the console
def clear(seconds=0):
    time.sleep(seconds)
    os.system('clear')


# Initializing an empty Dictionary
total_bids = {}

# Continue Condition
should_continue = True

# Welcome message and displaying ASCII Logo Art
print("Hello and Welcome to the Silent Auction.")
print(logo)

while should_continue:

    # Gathering user's inputs, and adding them as an entry to bidding dictionary
    usr_name = input("What is your name? ")
    usr_bid = int(input("How much are you bidding for this item? $"))
    total_bids[usr_name] = usr_bid

    # Continue-ing the auction or not
    should_continue = input("Are there any other users who want to bid? Press y/n: ").lower()

    # If the bid is finished
    if should_continue == "n":
        # Clear the console, initialize a variable for winner and the amount they bid
        clear()
        winner = ""
        winner_bid = 0

        # Looping through the keys of our total_bid dictionary
        for user in total_bids:
            # Assigning the person with the highest bid
            if total_bids[user] >= winner_bid:
                winner_bid = total_bids[user]
                winner = user

        # Capitalizing first character of winner's name
        winner = winner[0].upper() + winner[1:len(winner)]

        # Printing out win statement.
        print(f"The winner is {winner} with a bid of ${winner_bid}")
        # Exit our while loop
        should_continue = False
    # Continue the Auction
    else:
        clear(0)
