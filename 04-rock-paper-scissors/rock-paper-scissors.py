import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Storing images into a list, for easier access
game_images = [rock, paper, scissors]

# Gathering user input, and randomizing computer
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
comp_choice = random.randint(0, 2)

# Ensuring input is valid
if user_choice < 0 or user_choice > 2:
    print("You did not put in a valid response. You lose..")
    exit()

# Accessing game_images list with user and comp choice
print(game_images[user_choice])

print("Computer Choice:")
print(game_images[comp_choice])

# Rock 0 beats Scissors 2
# Scissors 2 beats Paper 1
# Paper 1 beats Rock 0

if user_choice == 0 and comp_choice == 2:
    print("You Win!")
elif user_choice == 2 and comp_choice == 1:
    print("You Win!")
elif user_choice == 1 and comp_choice == 0:
    print("You Win!")
elif user_choice == comp_choice:
    print("It's a Tie")
else:
    print("You Lose...")

