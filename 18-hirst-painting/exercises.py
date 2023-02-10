# Understanding the Turtle Graphics library and reading documentation
import random
import turtle as t
from random import choice

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
        turtle.color(random_color())


def random_walk(turtle, strokes):
    turtle.shape('arrow')
    turtle.pensize(8)
    turtle.speed('fast')
    for _ in range(strokes):
        turtle.fd(20)
        turtle.color(random_color())
        turtle.setheading(choice(direction))


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_col = (r, g, b)
    return random_col


def spirograph(turtle):
    turn_degree = 5
    turns = int(360 / turn_degree)
    turtle.speed('fastest')
    for _ in range(turns):
        turtle.color(random_color())
        turtle.setheading(turn_degree)
        turtle.circle(100)
        turn_degree += 5


tim = t.Turtle()

# Changing color mode so we can change to random colours
t.colormode(255)
tim.shape('turtle')
tim.color('blueviolet')

spirograph(tim)
screen = t.Screen()
screen.exitonclick()
