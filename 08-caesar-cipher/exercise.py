from math import ceil


# Coding Exercise 1 - Paint Area Calculator
def paint_calc(height, width, cover):
    num_of_cans = ceil((height * width) / cover)

    print(f"You'll need {num_of_cans} cans of paint")


paint_calc(2, 4, 5)


# Coding Exercise 2 - Prime Number Checker

# Solution # 1
def prime_checker(number):
    multiple_of_number = 0
    for i in range(1, number + 1):
        if number % i == 0:
            multiple_of_number += 1

    if multiple_of_number > 2:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


prime_checker(11)


# Solution
def prime_checker_2(number):
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")


prime_checker_2(11)
