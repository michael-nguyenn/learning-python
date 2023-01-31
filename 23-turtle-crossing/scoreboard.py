from turtle import Turtle

OVER_MESSAGE = "YOU SUCK"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.sety(260)
        self.pencolor('black')
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        message = f"Score: {self.score}"
        self.write(message, False, "left", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(OVER_MESSAGE, False, "center", FONT)
