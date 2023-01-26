# Event Listeners, State, and Multiple Instances

from turtle import Turtle, Screen

# Higher Order Functions & Event Listeners

tim = Turtle()

screen = Screen()


def move_forwards():
    tim.forward(10)


screen.listen()
# When passing in functions as arguments, we don't include the ()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()

# A higher order function can work with other functions. In our case above, move_forward is a higher
#   order function.
