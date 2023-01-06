import random

word_list = ["aardvark", "baboon", "camel"]

# SELECTING A RANDOM WORD, ASKING USER FOR THEIR INPUT, AND CHECKING IF THEIR INPUT MATCHES OR NOT

random_word = random.choice(word_list)

guess = input("Guess a character: ").lower()

for char in random_word:
    if char == guess:
        print(f"{guess} is correct")
    else:
        print(f"{guess} is wrong")
