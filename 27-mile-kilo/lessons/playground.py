# Unlimited Arguments

# The * tells python to accept n amount of arguments

# How can we modify the following add() function to take in unlimited arguments
def add(*args):
    total = 0
    for n in args:
        total += n

    return total


answer = add(1, 2, 3, 4, 5)


# This creates unlimited keyword arguments

# What will the following code output?
def calculate(n, **kwargs):
    # print(type(kwargs))  # kwargs

    n += kwargs["add"]
    n *= kwargs["multiply"]

    # print(n)  # 25


calculate(2, add=3, multiply=5)


# Create a car class that will take optional keyword arguments
class Car:
    def __init__(self, **kw):
        # Notice how we use the .get method. This will leave the attribute optional
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Tesla", model="3")
print(my_car.make)
