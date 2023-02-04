# Dictionary Comprehension - a way of creating a new dictionary

# new_dict = {new_key: new_value for item in list}

# new_dict = {new_key: new_value for (key,value) in dict.items()}

# Can add a condition as well
# new_dict = {new_key: new_value for (key,value) in dict.items() if test}

import random

students = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# Looped through a list to create a new dict
student_scores = {student: random.randint(50, 100) for student in students}

# Loop through an existing dict and create a new dict via comprehension
passed_students = {student: score for (student, score) in student_scores.items() if score > 60}

# print(student_scores)
# print(passed_students)
