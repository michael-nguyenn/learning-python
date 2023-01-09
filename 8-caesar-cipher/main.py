# Functions with input #########

# Simple Function
def greet():
    print('Hello Michael!')


# Function that allows for input
def greet_with_name(name):
    print(f'Hello {name}')
    print(f"Isn't it nice today {name}?")
    print(f"{name}, you forgot to poop today...")


# greet()
# greet_with_name("Michael")

# Function with more than 1 input. The parameters are positional arguments
def greet_with(name, location):
    print(f"Hello {name}, what is is like in {location}?")


greet_with("Michael", "Canada")

# Calling the function with keyword arguments instead of positional

greet_with(location="Banana Republic", name="Irene")

# list.index()
