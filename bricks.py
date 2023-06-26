import globals
from turtle import Turtle

LEFT_LIM = (globals.WIDTH / 2) * -1
RIGHT_LIM = globals.WIDTH / 2
UP_LIM = globals.HEIGHT / 2
DOWN_LIM = (globals.HEIGHT / 2) * -1

BRICK_WIDTH = globals.BRICK_SIZE * 20


class Brick(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.color('black', color)
        self.up()
        self.shape('square')
        self.shapesize(1, globals.BRICK_SIZE)
        self.goto(x=x, y=y)


def bricks_row(y, color):
    x = LEFT_LIM + (BRICK_WIDTH / 2)
    row = []
    while x <= RIGHT_LIM:
        brick = Brick(x, y, color)
        row.append(brick)
        x += BRICK_WIDTH
    return row
