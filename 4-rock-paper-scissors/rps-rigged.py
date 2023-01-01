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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if user_choice < 0 or user_choice > 2:
    print("You did not put in a valid response. You lose..")
    exit()


print(game_images[user_choice])


# Rock 0 beats Scissors 2
# Scissors 2 beats Paper 1
# Paper 1 beats Rock 0

if user_choice == 0:
    comp_choice = 1
elif user_choice == 1:
    comp_choice = 2
else:
    comp_choice = 0

print("Computer choice is:")
print(game_images[comp_choice])

print("You lose...")
