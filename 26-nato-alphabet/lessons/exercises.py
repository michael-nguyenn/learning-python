# Using List Comprehension, create a new list containing each squared number

numbers_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number ** 2 for number in numbers_1]
# print(squared_numbers)

# Using List Comprehension create a new list that only contains the even numbers

numbers_2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [number for number in numbers_2 if number % 2 == 0]
# print(result)


with open('file1.txt') as file:
    file_1 = [int(number) for number in (file.readlines()) if number != '\n']

with open('file2.txt') as file:
    file_2 = [int(number) for number in (file.readlines()) if number != '\n']

print(file_1)
print(file_2)

duplicate_values = [number for number in file_1 if number == number in file_2]

print(duplicate_values)

# Using Dictionary Comprehension, create a results dictionary that takes each word in the given sentence,
# and calculates the number of letters in each word.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

results = {word: len(word) for word in sentence.split(' ')}
print(results)

# Use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature
# in degrees Celsius and converts it into degrees Fahrenheit.

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp_c * 9 / 5) + 32 for day, temp_c in weather_c.items()}

print(weather_f)
