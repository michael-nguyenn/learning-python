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


my_function()


def my_function_fixed():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function_fixed()
