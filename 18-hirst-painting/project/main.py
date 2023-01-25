import colorgram
import random
import turtle as t

c = colorgram.extract('dots.jpg', 11)


def rgb_extractor(colors):
    palette = []

    for color in colors:
        rgb = color.rgb
        palette.append((rgb[0], rgb[1], rgb[2]))

    palette.pop(0)
    return palette


color_list = rgb_extractor(c)


def print_dots(turtle):
    for _ in range(10):
        turtle.dot(20, random.choice(color_list))
        turtle.penup()
        turtle.fd(50)
        turtle.pendown()


timmy = t.Turtle()
t.colormode(255)  # Changing color mode so we can change to random colours
timmy.penup()
timmy.setx(-100)
timmy.sety(-100)
timmy.pendown()
timmy.speed('fast')
y = -100

for _ in range(10):
    print_dots(timmy)
    timmy.penup()
    y += 50
    timmy.setpos(-100, y)
    timmy.pendown()

screen = t.Screen()
screen.exitonclick()
