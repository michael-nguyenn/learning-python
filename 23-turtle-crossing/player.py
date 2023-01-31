from turtle import Turtle
from time import sleep

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.fd(MOVE_DISTANCE)

    def has_crossed(self):
        if self.ycor() == FINISH_LINE_Y:
            sleep(0.1)
            self.goto(STARTING_POSITION)
