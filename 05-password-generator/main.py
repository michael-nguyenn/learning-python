# Loops

# For Loop - Loop through anything that is iterable. e.g. a range, a list, a dictionary, or tuple

fruits = ['Apple', 'Peach', 'Pear']

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

print(fruits)

# For loop and the range() function
total = 0

for number in range(1, 101):
    total += number

print(total)