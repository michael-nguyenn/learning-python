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
        self.following = 0

    # Creating a method
    def follow(self, user):
        user.followers += 1
        # The self keyword, similar to this, refers to the object that will be created from this class
        self.following += 1


user_1 = User("001", "michael")  # new user being created
user_2 = User("002", "irene")  # new user being created

# Creating attributes - not the best practice
user_1.test = True

# Calling the method
user_1.follow(user_2)

print(user_1.following)  # 1
print(user_1.followers)  # 0
print(user_2.followers)  # 1
