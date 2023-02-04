# List Comprehension - a case where you create a new list from an old list

# Example
# Normally if you want to increment each item by one, we'd have to loop through
# each number, add 1, and then append it to a new array
numbers = [1, 2, 3]
# syntax goes name = [new_item for item in items]
new_numbers = [n + 1 for n in numbers]

# print(new_numbers)  # [2, 3, 4]


# List comprehension isn't limited to list, we can do it with any sequence aka iterable

name = "Michael"
new_name = [letter.upper() for letter in name]

# print(new_name)  # ['M', 'I', 'C', 'H', 'A', 'E', 'L']

doubled_range = [i * 2 for i in range(1, 6)]

# print(doubled_range)  # [2, 4, 6, 8, 10]


# Conditional List Comprehension

# new_list = [new_item for item in list if test]

names = ["Michael", "Irene", "Henry", "Shirley", "Dominic"]

short_names = [name for name in names if len(name) <= 5]

# print(short_names)  # ['Irene', 'Henry']

long_names = [name.upper() for name in names if len(name) >= 5]

print(long_names)  # ['MICHAEL', 'IRENE', 'HENRY', 'SHIRLEY', 'DOMINIC']
