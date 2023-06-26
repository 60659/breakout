import globals
from turtle import Turtle
import random

LEFT_LIM = (globals.WIDTH / 2) * -1 + 10
RIGHT_LIM = globals.WIDTH / 2 - 12
UP_LIM = globals.HEIGHT / 2 - 10
DOWN_LIM = (globals.HEIGHT / 2) * -1 + 15


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#e9ecef")
        self.up()
        self.shapesize(0.5, 0.5)

    def ball_reset(self):
        self.showturtle()
        self.goto(x=-(random.randint(LEFT_LIM + 40, RIGHT_LIM - 40)), y=DOWN_LIM + 60)

    def ball_hide(self):
        self.hideturtle()
