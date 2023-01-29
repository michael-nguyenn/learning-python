# Breaking Down Pong

# Scoreboard class to keep track of the score
#    Create the dividing line
#    Max Score?? Maybe 12

# Create Paddles on each side, one for player, one for computer

# Create the pong block, that was generated randomly
#   It will bounce off the y-axis, but if it reaches the x-axis of one side, the score will increment the opponent
#   If it touches either paddles, it will bounce off at that angle
#   Once the score gets incremented, we then create a new block

import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.colormode(255)
screen.tracer(0)

l_paddle = Paddle(x_position=-350)
r_paddle = Paddle(x_position=350)
ball = Ball()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True

while game_is_on:
    # time.sleep(0.1)
    screen.update()

    ball.move()

screen.exitonclick()
