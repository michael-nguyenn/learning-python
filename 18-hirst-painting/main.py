# Understanding the Turtle Graphics library and reading documentation

from turtle import Turtle, Screen


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


tim = Turtle()
tim.shape('turtle')
tim.color('blueviolet')

draw_dashed_line(tim, 10)

screen = Screen()
screen.exitonclick()
