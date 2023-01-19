import sys
import data

money = 0.0


def resource_check(drink):
    """Checking if there are enough resources in the machine"""
    # TESTING CODE
    print("TESTING CODE - Resource Check is running...")

    # Accessing the ingredients keys from selected drink
    ingredients = data.MENU[drink]['ingredients']

    # This boolean variable ensures it will print out everything that is out of stock
    # For example if water, and milk are out of stock
    enough_ingredients = True

    # Looping through each key, and comparing their values to resources
    for ingredient in ingredients:

        # If resources doesn't have enough, we return False
        if ingredients[ingredient] > data.resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            enough_ingredients = False

    return enough_ingredients


def coffee_machine():
    functional = True

    while functional:
        # 1 - Prompt user by asking, "What would you like? (expresso/latte/cappuccino): "
        #  TODO - THIS PROMPT SHOULD SHOW EVERYTIME AN ACTION HAS BEEN COMPLETED
        user_input = input("What would you like? (espresso/latte/cappuccino): ")

        # TESTING CODE
        print(f"TESTING CODE - {user_input}")

        # 2 - Turn off Coffee Machine - "off"
        if user_input == 'exit':
            functional = False

        # 3 - Print Report - "report"
        if user_input == 'report':
            print(f"Water: {data.resources['water']}")
            print(f"Milk: {data.resources['milk']}")
            print(f"Coffee: {data.resources['coffee']}")
            print(f"Money: ${money}")

        # 4 - Checking if resources are sufficient
        if user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
            if not resource_check(user_input):
                functional = False

    # TESTING CODE
    print("TESTING CODE - Over")


coffee_machine()
