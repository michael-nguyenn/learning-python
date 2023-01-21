# import sys
import data
import time
from art import logo


def resource_check(drink):
    """Checking if there are enough resources in the machine"""
    # TESTING CODE
    # print("TESTING CODE - Resource Check is running...")

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


def coin_process():
    """Asks users for coins, and processes total amount"""
    print("Please insert your coins")
    amount = int(input("How many quarters?: ")) * 0.25
    amount += int(input("How many dimes?: ")) * 0.10
    amount += int(input("How many nickels?: ")) * 0.05
    amount += int(input("How many pennies?: ")) * 0.01

    return amount


def resources_avail(money):
    print(f"Water: {data.resources['water']}")
    print(f"Milk: {data.resources['milk']}")
    print(f"Coffee: {data.resources['coffee']}")
    print(f"Money: ${money}")


def brew(drink):
    """Loop through current drink, and subtract from resource"""

    ingredients = data.MENU[drink]['ingredients']

    for ingredient in ingredients:
        data.resources[ingredient] -= ingredients[ingredient]


def list_prices(menu):
    """Loop through each object, and print out cost"""
    for item in menu:
        print(f"{item.capitalize()} costs ${menu[item]['cost']}")


def coffee_machine():
    print(logo)
    print("Would you like a hot drink?")
    time.sleep(1)
    list_prices(data.MENU)

    money = 0.0
    functional = True

    while functional:

        # 1 - Prompt user by asking, "What would you like? (expresso/latte/cappuccino): "
        #  Prompt will show everytime we complete an action
        user_input = input("What would you like? (espresso/latte/cappuccino): ")

        # TESTING CODE
        # print(f"TESTING CODE - {user_input}")

        # 2 - Turn off Coffee Machine - "off"
        if user_input == 'exit':
            functional = False

        # 3 - Print Report - "report"
        if user_input == 'report':
            resources_avail(money)

        # 4 - Checking if resources are sufficient
        if user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
            if not resource_check(user_input):
                functional = False
            else:
                refund = True
                item_price = data.MENU[user_input]["cost"]

                while refund:
                    # 5 - Processing coins
                    user_cash = coin_process()

                    # TESTING CODE
                    # print(f"TESTING CODE - {user_cash}")

                    # 6 - Check if transaction is successful
                    if item_price > user_cash:
                        print("Sorry that's not enough money. Money refunded")
                    else:
                        print(f"Here is ${round((user_cash - item_price), 2)} in change")
                        refund = False

                # 7 - MAKE COFFEE
                print(f"Report before purchasing {user_input}")
                time.sleep(1)
                resources_avail(money)
                print(f"--- BREWING UP YOUR {user_input.upper()} ---")
                time.sleep(1)
                brew(user_input)
                money += item_price
                print(f"Report after purchasing {user_input}:")
                time.sleep(1)
                resources_avail(money)


coffee_machine()
