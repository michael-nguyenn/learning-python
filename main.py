from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snaaaaaaaaake")

# Turns off screen to generate snake
screen.tracer(0)

# Creating snake body
snake = []


def snake_factory():
    y = 0
    x = 0
    for i in range(3):
        snake.append(Turtle('square'))
        snake[i].color('white')
        snake[i].penup()
        snake[i].goto(x, y)
        x -= 20


snake_factory()
# screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    # We iterate downwards from bottom of snake
    for seg_num in range(len(snake) - 1, 0, -1):
        # We assign x,y co-ords to the previous
        # For example segment three, will become segment two, in terms of co-ords
        new_y = snake[seg_num - 1].ycor()
        new_x = snake[seg_num - 1].xcor()
        snake[seg_num].goto(new_x, new_y)

    snake[0].fd(20)

screen.exitonclick()
