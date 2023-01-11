from art import logo

# Displaying our nice logo
print(logo)


# Arithmetic Operations
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Dictionary containing the operations as keys and the functions as the values
operations = {
    "+": add,  # function value
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    # Gathering user input
    num1 = float(input("What's the first number?: "))

    # Displaying all available operations
    for operation in operations:
        print(operation)

    # Setting Continue Condition
    should_continue = True

    while should_continue:
        # Gathering user input
        operation_symbol = input("Please pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))

        # Retrieving the function via user input, and immediately invoking it with (num1, num2)
        answer = operations[operation_symbol](num1, num2)

        # Showing the calculation in the console
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Continue condition
        next_calculation = input(f"Type 'y' to continue calculating with {answer},"
                                 f" or type 'n' to start a new calculation: ")

        # Exit the Loop if user selects n
        if next_calculation == 'n':
            should_continue = False

            # Using recursion to restart the calculator
            calculator()
        else:
            # We restart our while loop
            # Turning num1 to answer so that we can chain our operations
            num1 = answer


calculator()
