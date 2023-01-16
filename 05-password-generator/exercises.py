# Calculating the average height of students.
# Do not use sum() or len()
student_heights = [180, 124, 165, 173, 189, 169, 146]
total_height = 0
total_students = 0

for student in student_heights:
    total_height += student
    total_students += 1

print(round(total_height / total_students))

# Calculate the highest score from a list of scores
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
high_score = student_scores[0]

for score in student_scores:
    if score >= high_score:
        high_score = score

print(f"The highest score in the class is: {high_score}")

# Calculate the sum of all even numbers from 1-100

total_even = 0

for number in range(2, 101, 2):
    total_even += number

print(total_even)

# FizzBuzz

for number in range(1, 101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
