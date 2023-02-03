import turtle
import pandas

correct_turtle = turtle.Turtle()
correct_turtle.hideturtle()
screen = turtle.Screen()

screen.title("U.S. States Game")

# Setting background to a map
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def draw_state(x, y, state):
    correct_turtle.penup()
    correct_turtle.goto(x, y)
    correct_turtle.pendown()
    correct_turtle.write(state)


# Initializing an array to store correct guesses
correct_states = []
correct_guesses = 0

# Reading Data from CSV file
data = pandas.read_csv('50_states.csv')

while correct_guesses < 50:
    title = f"{correct_guesses}/50 States Correct"
    # Prompting users for their answer and setting it to Title Case
    answer_state = screen.textinput(title=title, prompt="What's another state's name: ").title()

    if answer_state == "Exit":
        # Save and write missing states to a new CSV file
        states_list = data.state.tolist()

        for state in correct_states:

            if state in states_list:
                states_list.remove(state)

        missing_states = {
            "State": states_list
        }

        data_export = pandas.DataFrame(missing_states)
        data_export.to_csv('missing_states.csv')

        break

    # Searching for the correct row matching user's guess
    matching_state = data[data["state"] == answer_state]

    # If the result comes up empty, that means the user guessed wrong, otherwise
    #   draw state in its corresponding location
    if len(matching_state) > 0 and answer_state not in correct_states:
        x_coord = matching_state.x.tolist()[0]
        y_coord = matching_state.y.tolist()[0]

        # Draw the state on the board
        draw_state(x_coord, y_coord, answer_state)

        # Store the correct state into an array
        correct_states.append(answer_state)
        # Update the score
        correct_guesses = len(correct_states)


