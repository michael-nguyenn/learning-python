from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# Make 6 turtles in 6 different colours, all end up at -235 x and evenly spaced for y
turtles = []


def turtle_factory():
    x = -235
    y = -120

    for i in range(len(colors)):
        turtles.append(Turtle(shape="turtle"))
        turtles[i].color(colors[i])
        turtles[i].penup()
        turtles[i].goto(x, y)
        y += 50


turtle_factory()

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner!")

        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
