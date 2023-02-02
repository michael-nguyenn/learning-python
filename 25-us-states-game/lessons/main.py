# Using cvs library to extract tabular data
# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] == "temp":
#             pass
#         else:
#             temperatures.append(int(row[1]))


# Using pandas library to achieve the same
import pandas

# Data is Dataframe type
data = pandas.read_csv("weather_data.csv")

# Getting Data in Columns
temp_series = data.temp
max_temp = temp_series.max()

# Getting Data in Rows
# print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]

mon_temp_F = int(monday.temp)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("new_data.csv")
