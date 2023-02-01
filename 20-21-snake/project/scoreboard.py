from turtle import Turtle

ALIGNMENT = "center"
OVER_MESSAGE = "Ooopsies"
FONT = ("Courier", 24, "normal")

with open("data.txt", mode="r") as file:
    HIGH_SCORE = int(file.read())


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = HIGH_SCORE
        self.hideturtle()
        self.sety(250)
        self.pencolor("white")
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        message = f"Score: {self.score} High Score: {self.high_score}"
        self.write(message, False, ALIGNMENT, FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(OVER_MESSAGE, False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", mode="w") as doc:
                doc.write(str(self.high_score))

        self.score = 0
        self.update_score()
