# Scope ####

# Namespaces: Local vs. Global Scope

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()  # enemies inside function: 2
print(f"enemies outside function: {enemies}")  # enemies outside function: 1

# Local Scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
#
# drink_potion()  # 2
# print(potion_strength)  # Error

# Global Scope

player_heath = 10


def drink_potion():
    potion_strength = 2
    print(player_heath)


drink_potion()  # 10

# Does Python have Block Scope?? => Nope ######

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)  # Skeleton

# Constants and Global Scope

# Naming Convention for global constants is SCREAMING_SNAKE_CASE
PI = 3.14159
TWITTER_HANDLE = "@blah"

# Quiz

i = 50


def foo():
    i = 100
    return i


foo()
print(i)  # 50


def bar():
    my_variable: 9

    if 16 > 9:
        my_variable = 16

    print(my_variable)


bar()  # 16
