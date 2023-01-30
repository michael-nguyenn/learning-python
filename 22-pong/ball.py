from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = 1
        self.y_move = 1
        self.choice = [1, -1]

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto((new_x, new_y))

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.increase_speed()

    def reset_position(self):
        self.home()
        self.x_move = random.choice([-1, 1])
        self.y_move = random.choice([-1, 1])

    def increase_speed(self):
        self.x_move *= 1.2
        self.y_move *= 1.2
