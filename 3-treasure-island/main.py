# Control Flow with if / else and Conditional Operators
water_level = 80

if water_level >= 50:
    print("Drain Water...")
else:
    print("Continue-ing on")

print("Welcome to the roller-coaster!")
# height = int(input("What is your name in cm? "))
# age = int(input("What is your age? "))
height = 129
age = 50
bill = 0

if height >= 120:
    print("You can ride")
    if age < 12:
        print("Child Tickets are 5$")
        bill = 5
    elif 12 <= age <= 18:
        print("Youth ticket are 7$")
        bill = 7
    elif 45 <= age <= 55:
        print("Don't worry about your midlife crisis, your ticket is free!")
        bill = 0
    else:
        print("Adult ticket costs 12$")
        bill = 12

    # wants_photo = input("Do you want a photo taken? Y or N. ")
    wants_photo = "Y"
    if wants_photo == "Y":
        bill += 3

    print(f"Your total cost is {bill}$")

else:
    print("You are too short to ride. Please grow more!")

# Comparison Operators
# > Greater than
# etc...
# Modulo % operator

# Logical Operators
# and, or , not

# .lower() .count()

