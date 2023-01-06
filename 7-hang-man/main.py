import random

# Step 1

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

random_word = random.choice(word_list)
print(random_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Please guess a character: ").lower()

print(guess)

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for char in random_word:
    if char == guess:
        print(f"{guess} is correct")
    else:
        print(f"{guess} is wrong")
