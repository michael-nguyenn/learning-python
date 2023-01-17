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
year = int(input("What's your year of birth? "))
if 1980 < year <= 1994:
    print("You are a Millennial.")
elif year > 1994:
    print("You are a Gen Z.")
