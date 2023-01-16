# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# nr_letters = 4
# nr_numbers = 2
# nr_symbols = 2
total_list = []

# Without Loops ######

# total_list = random.sample(letters, nr_letters) + random.sample(numbers, nr_numbers) + \
#              random.sample(symbols, nr_symbols)

# Using Loop #########

# Looping in range of nr_letters
for i in range(1, nr_letters + 1):
    # Generating a random index from letters, and appending to a list
    total_list.append(letters[random.randint(0, len(letters) - 1)])

    # Range function provides same effect, just use of different syntax
for i in range(nr_numbers):
    total_list.append(numbers[random.randint(0, len(numbers) - 1)])

    # Instead of randint(), choice() can be used for readability
for i in range(nr_symbols):
    total_list.append(random.choice(symbols))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

print(''.join(total_list))

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random.shuffle(total_list)
print(''.join(total_list))
