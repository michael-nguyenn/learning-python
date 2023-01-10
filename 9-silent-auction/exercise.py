# GRADING PROGRAM
# Converting student's scores to grades

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


def grading_program(scores):
    # Initializing an empty dictionary for end result
    student_grades = {}

    for student in scores:
        if scores[student] >= 91:
            student_grades[student] = "Outstanding"
        elif 81 <= scores[student] <= 90:
            student_grades[student] = "Exceeds Expectations"
        elif 71 <= scores[student] <= 80:
            student_grades[student] = "Acceptable"
        else:
            student_grades[student] = "Fail"

    return student_grades


student_grades = grading_program(student_scores)
