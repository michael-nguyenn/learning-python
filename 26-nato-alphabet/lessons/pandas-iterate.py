# A Pandas dataframe is in a lot of ways similar to a python library

import pandas

student_dict = {
    "student": ["Michael", "Irene", "Henry"],
    "score": [90, 80, 69]
}

student_data_frame = pandas.DataFrame(student_dict)

# print(student_data_frame)

# Loop through a data frame

# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# Loop through rows of data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)
