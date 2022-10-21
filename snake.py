from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270

class Snake:

    def __init__(self):
        self.main_snake = []
        self.create_snake()
        self.head = self.main_snake[0]

    def create_snake(self):

        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.main_snake.append(snake)

    def reset(self):
        for seg in self.main_snake:
            seg.goto(1000, 1000)
        self.main_snake.clear()
        self.create_snake()
        self.head = self.main_snake[0]

    def extend(self):
        self.add_segment(self.main_snake[-1].position())

    def move(self):
        for seg_num in range(len(self.main_snake) - 1, 0, -1):
            new_x = self.main_snake[seg_num - 1].xcor()
            new_y = self.main_snake[seg_num - 1].ycor()
            self.main_snake[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
