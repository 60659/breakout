from turtle import Turtle
import globals

position_x = -(globals.WIDTH / 2) + 10
position_y = (globals.HEIGHT / 2) - 25


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.color("white")
        self.goto(x=position_x, y=position_y)

    def set(self, score):
        self.clear()
        self.write(f"Score: {score}", font=("Courier", 15, "normal"), align="left")
