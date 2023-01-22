# INTRODUCTION TO OOP
# Splits larger tasks into smaller pieces
#   Imagine being tasked for running a restaurant
#   Think of the different roles of a restaurant - greeter, waiter, chef, server
#       Each of these roles, have specific tasks at hand, and you just have to manage them


# Breaking down the roles (classes) - think about what the class has / does

# Waiter:
#   has (attributes): is_holding_plate = True, tables_responsible = [4,5,6]
#   does (methods): def take_order(table,order): , def take_payment(amount):

# Once we've modelled our object (blueprint), we can generate as many copies (objects) of these as we need

from turtle import Turtle, Screen

# Constructing our object - based on the Turtle class, from the turtle library
timmy = Turtle()

timmy.shape('turtle')
timmy.color('deepskyblue')
timmy.fd(100)

# To access attributes - car.speed
my_screen = Screen()
print(my_screen.canvheight)

# To call methods - car.stop()
my_screen.exitonclick()
