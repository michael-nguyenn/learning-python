# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Reading the file

with open("../project/input/letters/starting_letter.txt") as file:
    # Readlines returns a list containing each line in the file
    # The parameter limits the number of lines returned. If the total bytes returned exceeds the number,
    # no more lines are returned
    letter = file.read()

# Testing code
# x = txt.replace("[name]", "Test")
#
# print(x)

with open("../project/Input/Names/invited_names.txt") as file:
    invited_people = file.readlines()

for person in invited_people:
    # Strip method removes and leading and trailing spaces
    invitee = person.strip()

    with open(f"../project/Output/ReadyToSend/{invitee}.txt", mode="w") as file:
        file.write(letter.replace("[name]", invitee))
