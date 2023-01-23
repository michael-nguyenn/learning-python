# Class Syntax

# pass keyword tells python to continue onto the next line of code

# Naming convention for python classes is PascalCase

# A Constructor (initializing) allows us to set (variables, counters, switches etc)
#   to their starting values at the beginning of a program
#   This can be done via the __init__ function
class User:
    # Inside this constructor function is where we initialize our attributes
    # This function runs everytime an instance gets made
    def __init__(self, user_id, username):
        print("new user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0  # Providing a default value


user_1 = User("001", "michael")
user_2 = User("002", "irene")

# Creating attributes - not the best practice
user_1.test = True
