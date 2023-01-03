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
