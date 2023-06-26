import globals
from turtle import Screen
from paddle import Paddle
from bricks import bricks_row
from ball import Ball
from random import choice
from score import Score
from time import sleep

game_is_on = True

# screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=globals.WIDTH, height=globals.HEIGHT)
screen.title("Breakout")
screen.tracer(0)

# score
score = Score()
points = 0
score.set(points)


def point():
    global points
    points += 1
    score.set(points)


# paddle
paddle = Paddle()

# paddle moves
screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

# ball
ball = Ball()
ball.ball_reset()
LEFT_LIM = (globals.WIDTH / 2) * -1 + 10
RIGHT_LIM = globals.WIDTH / 2 - 12
UP_LIM = globals.HEIGHT / 2 - 10
DOWN_LIM = (globals.HEIGHT / 2) * -1 + 15
delta_x = choice([-1, 1])
delta_y = 1


def move():
    global delta_x, delta_y
    if ball.xcor() > RIGHT_LIM or ball.xcor() < LEFT_LIM:
        delta_x *= -1
    if ball.ycor() > UP_LIM:
        delta_y *= -1

    new_x = ball.xcor() + delta_x
    new_y = ball.ycor() + delta_y
    ball.setx(new_x)
    ball.sety(new_y)


def paddle_bounce():
    global delta_x, delta_y
    # ball from top
    if (ball.ycor() == paddle.ycor() + globals.BALL_SIZE and
            paddle.xcor() - globals.PADDLE_X < ball.xcor() < paddle.xcor() + globals.PADDLE_X):
        delta_y *= -1
    # ball from left
    elif (ball.xcor() == paddle.xcor() - globals.PADDLE_X and
            paddle.ycor() - globals.PADDLE_Y < ball.ycor() < paddle.ycor() + globals.PADDLE_Y):
        delta_x *= -1
    # ball from right
    elif (ball.xcor() == paddle.xcor() + globals.PADDLE_X and
            paddle.ycor() - globals.PADDLE_Y < ball.ycor() < paddle.ycor() + globals.PADDLE_Y):
        delta_x *= -1


# bricks
all_bricks = []


def create_bricks():
    global all_bricks
    y = 40
    rows = ['#1be7ff', '#6EEB83', '#E4FF1A', '#FFB800', '#FF5714']

    for row in rows:
        all_bricks.extend(bricks_row(y, row))
        y += 20


create_bricks()


def brick_collision():
    global delta_x, delta_y
    for brick in all_bricks:
        # ball from bottom
        if (ball.ycor() == brick.ycor() - globals.BRICK_Y and
                brick.xcor() - globals.BRICK_X < ball.xcor() < brick.xcor() + globals.BRICK_X):
            brick.hideturtle()
            all_bricks.remove(brick)
            point()
            delta_y *= -1
        # ball from top
        elif (ball.ycor() == brick.ycor() + globals.BRICK_Y and
                brick.xcor() - globals.BRICK_X < ball.xcor() < brick.xcor() + globals.BRICK_X):
            brick.hideturtle()
            all_bricks.remove(brick)
            point()
            delta_y *= -1
        # ball from left
        elif (ball.xcor() == brick.xcor() - globals.BRICK_X and
                brick.ycor() - globals.BRICK_Y < ball.ycor() < brick.ycor() + globals.BRICK_Y):
            brick.hideturtle()
            all_bricks.remove(brick)
            point()
            delta_x *= -1
        # ball from right
        elif (ball.xcor() == brick.xcor() + globals.BRICK_X and
                brick.ycor() - globals.BRICK_Y < ball.ycor() < brick.ycor() + globals.BRICK_Y):
            brick.hideturtle()
            all_bricks.remove(brick)
            point()
            delta_x *= -1


def fail_reset():
    global delta_x, delta_y
    if ball.ycor() < DOWN_LIM - 100:
        ball.ball_reset()
        delta_x = choice([-1, 1])
        delta_y = 1


def bricks_reset():
    global all_bricks
    if not all_bricks:
        screen.update()
        sleep(2)
        ball.ball_hide()
        create_bricks()
        screen.update()
        sleep(2)
        ball.ball_reset()


while game_is_on:
    screen.update()
    paddle_bounce()
    brick_collision()
    bricks_reset()
    fail_reset()
    # screen.ontimer(move, 1)
    move()

screen.exitonclick()
