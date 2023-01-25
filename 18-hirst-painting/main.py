# Understanding the Turtle Graphics library and reading documentation

from turtle import Turtle, Screen
from random import choice

colors = ['SkyBlue', 'Aquamarine', 'indigo', 'DeepPink', 'Tomato', 'DarkOrchid', 'LightSeaGreen', 'SlateGray']
direction = [0, 90, 180, 270]


# Challenge #1 - Draw a square
def draw_square(turtle, distance):
    """Will draw a square with the specified distance"""
    for _ in range(4):
        turtle.fd(distance)
        turtle.right(90)


# Challenge # 2 - Draw a dashed line
def draw_dashed_line(turtle, lines):
    """The amount of dashed lines you want to draw"""
    for _ in range(lines):
        turtle.fd(10)
        turtle.penup()
        turtle.fd(10)
        turtle.pendown()


def draw_shapes(turtle):
    # Want range to increment 1 each time
    # while modulus of 360 % n is 0, then run the function

    n = 3

    while n <= 10:
        for _ in range(n):
            turtle.fd(100)
            turtle.right(360 / n)
        n += 1
        turtle.color(choice(colors))


def random_walk(turtle, strokes):
    turtle.shape('arrow')
    turtle.pensize(8)
    turtle.speed('fast')
    for _ in range(strokes):
        turtle.fd(20)
        turtle.color(choice(colors))
        turtle.setheading(choice(direction))


tim = Turtle()
tim.shape('turtle')
tim.color('blueviolet')

random_walk(tim, 200)

screen = Screen()
screen.exitonclick()
