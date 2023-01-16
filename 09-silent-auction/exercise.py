# EXERCISE 1 - GRADING PROGRAM
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


grades = grading_program(student_scores)

# EXERCISE 2 - TRAVEL LIST (DICTIONARY IN A LIST)
# Program that will allow new countries to be added to the travel_log

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country, visits, cities):
    country = {
        "country": country,
        "visits": visits,
        "cities": cities
    }

    travel_log.append(country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)
