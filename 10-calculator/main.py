# Functions with Output

# Using the return keyword will take the variable and the value of the function becomes the return value
def my_function() -> int:
    result = 3 * 2
    return result


output = my_function()  # 6


# Changing the word to title case
# Using the str.title()
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Please input a valid input"

    return f_name.title() + " " + l_name.title()


my_name = format_name("Michael", "NGUYEN")  # Michael Nguyen
# print(my_name)
