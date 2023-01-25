# Understanding the Turtle Graphics library and reading documentation

from turtle import Turtle, Screen


def move_in_square(turtle, distance):
    for _ in range(4):
        turtle.fd(distance)
        turtle.right(90)


tim = Turtle()
tim.shape('turtle')
tim.color('blueviolet')

move_in_square(tim, 100)

screen = Screen()
screen.exitonclick()
