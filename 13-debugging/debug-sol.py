from random import randint


# Steps in Debugging

# 1. Describe Problem

# What is the for-loop doing?
#   The for loop is looping from 1 (inclusive) to 20 (exclusive) aka 1-19

# When is the function meant to print "You got it?"
#   When "i" is equal to 20

# What assumptions are you making about the value of i
#   We're assuming it goes all the way to 20, which in this case it doesn't
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


# my_function()


def my_function_fixed():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


# my_function_fixed()

# 2. Reproduce the Bug

# The print statement will run fine 5/6 times, but 1/6 will give you an index out of range error.
# To reproduce it, we need to figure out, at which index it's giving us the problem
#   This code will never print 1, and when it tries to access 6, the index is out of range

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# print(dice_imgs[6])  # This code will always yield an error


# 3. Play Computer

# What happens when we input 1994 in the code?
#   Nothing will print

# The reason is that at the moment, we are not accounting for 1994 at all
#   To fix this, we must either classify 1994 as Millennial or Gen Z, by using the GTE or LTE operator

# year = int(input("What's your year of birth? "))
year = 1994
if 1980 < year <= 1994:
    print("You are a Millennial.")
elif year > 1994:
    print("You are a Gen Z.")

# 4. Fix the Errors
# In the below there are 3 problems
#   1. We need to convert age to int
#   2. We have to indent our print statement to nest inside the if block
#   3. Our print statement needs to be converted into an f string

# age = int(input("How old are you? "))
age = 15

if age > 18:
    print(f"You can drive at age {age}.")

# 5. Print is Your Friend
# Using print, we can see that initially we are using the equality equal signs (==)
#   instead of assignment equal sign (=). That creates a bug where word_per_page will always equal to 0
#   That means total_words will always be pages * 0 = 0

pages = 0
word_per_page = 0
print(f"FIRST PRINT: {pages} {word_per_page}")

pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
print(f"SECOND PRINT: {pages} {word_per_page}")

total_words = pages * word_per_page
print(total_words)
