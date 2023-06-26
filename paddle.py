import globals
from turtle import Turtle

LEFT_LIM = (globals.WIDTH / 2) * -1
RIGHT_LIM = globals.WIDTH / 2
UP_LIM = globals.HEIGHT / 2
DOWN_LIM = (globals.HEIGHT / 2) * -1


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        pos_x = 0
        pos_y = DOWN_LIM + 40
        self.shape('square')
        self.color('#e9ecef')
        self.up()
        self.goto(x=pos_x, y=pos_y)
        self.shapesize(1, globals.PADDLE_SIZE)

    def move_left(self):
        new_x = self.xcor() - globals.MOVEMENT
        if new_x >= LEFT_LIM + (globals.PADDLE_WIDTH / 2):
            self.setx(new_x)

    def move_right(self):
        new_x = self.xcor() + globals.MOVEMENT
        if new_x <= RIGHT_LIM - (globals.PADDLE_WIDTH / 2):
            self.setx(new_x)
