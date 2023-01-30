# Breaking Down Pong

# Scoreboard class to keep track of the score
#    Create the dividing line
#    Max Score?? Maybe 12

# Create Paddles on each side, one for player, one for computer

# Create the pong block, that was generated randomly
#   It will bounce off the y-axis, but if it reaches the x-axis of one side, the score will increment the opponent
#   If it touches either paddles, it will bounce off at that angle
#   Once the score gets incremented, we then create a new block


from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.colormode(255)
screen.tracer(0)

l_paddle = Paddle(x_position=-350)
r_paddle = Paddle(x_position=350)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()

    # Detecting Collision
    if ball.ycor() > 285 or ball.ycor() < -285:
        # Needs to bounce
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Detecting R paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detecting L paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
