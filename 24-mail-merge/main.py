# Open, Read and Write Files using "with" keyword

# Retrieve and read a text file called my_file.txt

# First retrieve the file and save it to a variable named file
file = open("my_file.txt")

# Read the contents of the file and save it to a variable
contents = file.read()

# We have to close its content, to free up memory
file.close()

# Printing out the contents in the terminal
print(contents)

# Using the with and as keyword we are able to shorten the syntax
# Note how we don't have to explicitly close the content anymore
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Writing a text file called my_file.txt

with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")  # with mode = "w" this rewrites the entire document

# When we open a non-existent file in write mode, we will create that said file
with open("new_file.txt", mode="w") as file:
    file.write("Look at me i'm writing into a new file")
