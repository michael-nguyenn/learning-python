from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.snake_factory()
        self.head = self.snake[0]

    def snake_factory(self):
        y = 0
        x = 0
        for i in range(3):
            self.snake.append(Turtle('square'))
            self.snake[i].color('white')
            self.snake[i].penup()
            self.snake[i].goto(x, y)
            x -= 20

    def move(self):
        # We iterate downwards from bottom of snake
        for seg_num in range(len(self.snake) - 1, 0, -1):
            # We assign x,y co-ords to the previous
            # For example segment three, will become segment two, in terms of co-ords
            new_y = self.snake[seg_num - 1].ycor()
            new_x = self.snake[seg_num - 1].xcor()
            self.snake[seg_num].goto(new_x, new_y)

        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
