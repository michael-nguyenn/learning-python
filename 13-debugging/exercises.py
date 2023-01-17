# DEBUGGING PROBLEMS

# Odd or Even

# number = int(input("Which number do you want to check?"))
#
# if number % 2 = 0: # assignment operator used instead of equality
#     print("This is an even number.")
# else:
#     print("This is an odd number.")


number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# Leap Year

# year = input("Which year do you want to check? ") # we are trying to insert str into our conditional statements
#
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")


year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

# Fizz Buzz
# Two Bugs:
#   1. In the first if statement, it has to be the and operator, otherwise it'll print "FizzBuzz" for all
#   2. The later two if statements need to be converted to elif, otherwise the else at the bottom
#       will print all digits from 1-100 no matter what.

# for number in range(1, 101):
#     if number % 3 == 0 or number % 5 == 0:
#         print("FizzBuzz")
#     if number % 3 == 0:
#         print("Fizz")
#     if number % 5 == 0:
#         print("Buzz")
#     else:
#         print([number])

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print([number])
