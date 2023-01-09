from math import ceil


# Coding Exercise 1 - Paint Area Calculator
def paint_calc(height, width, cover):
    num_of_cans = ceil((height * width) / cover)

    print(f"You'll need {num_of_cans} cans of paint")


paint_calc(2, 4, 5)
