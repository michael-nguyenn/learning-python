import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import random
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

# This initializes the car manager class
car_manager = CarManager()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Since our while loop runs at a 0.1s delay, it will generate a new car and call the move function
    car_manager.create_car()
    car_manager.move_cars()

    # Detecting successful crossing
    if player.has_crossed():
        scoreboard.increase_score()
        player.go_to_start()
        time.sleep(0.5)

    # Detecting collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
