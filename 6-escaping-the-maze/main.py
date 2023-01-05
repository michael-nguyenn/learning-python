# Defining and Calling Python Functions

# Functions allow you to give a set of instructions a name, so you can trigger it multiple times
# without having to rewrite it.

def my_function():
    print("Hello")
    name = "Michael"
    print(f"Hello {name}")


my_function()

# While Loop - Continue running while a particular condition is true
# While loops are useful when you have something that will eventually switch to false

countdown = 10

while countdown > 0:
    countdown -= 1
    print(countdown)

    if countdown == 0:
        print("BOOM")
