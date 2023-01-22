from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
# menu_item = MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def coffee_machine():
    functional = True

    while functional:

        # 1 - Prompt user by asking, "What would you like? (expresso/latte/cappuccino): "
        user_input = input("What would you like? (espresso/latte/cappuccino): ")

        # 2 - Turn off Coffee Machine - "off"
        if user_input == 'exit':
            functional = False

        # 3 - Print Report - "report"
        if user_input == 'report':
            coffee_maker.report()
            money_machine.report()

        if user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
            # Returns MenuItem object if drink exists
            drink = menu.find_drink(user_input)

            # 4 - Checking if resources are sufficient
            if not coffee_maker.is_resource_sufficient(drink):
                functional = False
            else:
                refund = True

                while refund:
                    # 5 - Processing coins
                    # 6 - Check if transaction is successful
                    money_machine.make_payment(drink.cost)
                    refund = False

                # 7 - MAKE COFFEE
                print(f"Report before purchasing {user_input}")
                coffee_maker.report()
                money_machine.report()
                print(f"--- BREWING UP YOUR {user_input.upper()} ---")
                coffee_maker.make_coffee(drink)
                print(f"Report after purchasing {user_input}:")
                coffee_maker.report()
                money_machine.report()


coffee_machine()
