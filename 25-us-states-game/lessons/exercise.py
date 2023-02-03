# The Great Squirrel Census Data Analysis

# Need to create a Dataframe with two columns
#   Fur Color, and Count

import pandas

# Grabbing the data as the Dataframe type
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

# Targeting the Fur Color column, and converting it from series to list
fur_colors = data["Primary Fur Color"].tolist()

grey_count = 0
cinnamon_count = 0
black_count = 0

for color in fur_colors:
    if color == "Gray":
        grey_count += 1

    if color == "Cinnamon":
        cinnamon_count += 1

    if color == "Black":
        black_count += 1

# Formatting data into each respective column and row values via dictionary
fur_color_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_count, cinnamon_count, black_count]
}

# Turning dict into a Dataframe type, and writing to a new CSV file
data_frame = pandas.DataFrame(fur_color_dict)
data_frame.to_csv("squirrel_count.csv")

# This is an alternate way of achieving the same result
# This targets the rows with the specific value where fur color is black
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
