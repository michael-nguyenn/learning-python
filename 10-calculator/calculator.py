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

# Gathering user input
num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

# Displaying all available operations
for operation in operations:
    print(operation)

# Gathering user input
operation_symbol = input("Please pick an operation from the line above: ")

# Retrieving the function via user input, and immediately invoking it with (num1, num2)
answer = operations[operation_symbol](num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
