# Dictionaries ! aka objects ###########

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Accessing elements from the dictionary - Subscripting
prog_bug = programming_dictionary["Bug"]
print(prog_bug)

# Adding a key to your dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# One way of clearing user's progress, etc...
# programming_dictionary = {}


# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"

# Looping through a dictionary
# Loops through keys in dictionary
for key in programming_dictionary:
    print(key)
    # Using the key to loop through it's values
    print(programming_dictionary[key])

# Nesting Lists and Dictionaries ########

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting Dictionary in a Dictionary

travel_log_two = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 8,
    },
}

travel_log_three = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 8
    },
]
