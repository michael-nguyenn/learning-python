from turtle import Turtle
import random


# Inheriting from Turtle class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    @staticmethod
    def random_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        random_col = (r, g, b)
        return random_col

    def refresh(self):
        random_x = random.randint(-285, 285)
        random_y = random.randint(-285, 285)
        self.color(self.random_color())
        self.goto(random_x, random_y)
