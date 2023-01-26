# Event Listeners, State, and Multiple Instances

from turtle import Turtle, Screen

# Higher Order Functions & Event Listeners

tim = Turtle()

screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_counter():
    tim.left(10)


def move_clockwise():
    tim.right(10)


def clear():
    tim.reset()


screen.listen()
# When passing in functions as arguments, we don't include the ()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()

# A higher order function can work with other functions. In our case above, move_forward is a higher
#   order function.
