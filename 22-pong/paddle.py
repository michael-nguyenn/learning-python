from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.x = x
        self.goto(x=x, y=0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
