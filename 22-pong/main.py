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

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.colormode(255)

screen.exitonclick()
