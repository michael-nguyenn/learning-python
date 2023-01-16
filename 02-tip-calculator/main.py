# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print("Welcome to the tip calculator")
total = input("What was the total bill? $")
tip_percentage = input("What % tip would you like to give? 10, 12, or 15? ")
amount_of_people = input("How many people to split the bill? ")

total_float = float(total)
tip_float = float(tip_percentage)
people_float = float(amount_of_people)

pay_per_person = "{:.2f}".format(total_float * ((tip_float + 100) / 100) / people_float)

print(f"Each person should pay: ${pay_per_person}")

