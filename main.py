from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snaaaaaaaaake")

# Creating snake body
snake = []


def snake_factory():
    y = 0
    x = 0
    for i in range(3):
        snake.append(Turtle('square'))
        snake[i].color('white')
        # snake[i].penup()
        snake[i].goto(x, y)
        x -= 20


snake_factory()

screen.exitonclick()
