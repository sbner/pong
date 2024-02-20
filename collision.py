from turtle import Screen
from ball import Ball
from paddle import Paddle

THRESHOLD = 10


def with_wall(screen: Screen, ball: Ball):
    distance_from_wall = (screen.screensize()[1] - THRESHOLD) - abs(ball.ycor())
    return distance_from_wall <= THRESHOLD


def with_paddle(paddle: Paddle, ball: Ball):
    abs_paddle_x_position = abs(paddle.position()[0])
    x_distance_from_paddle = (abs_paddle_x_position - THRESHOLD) - abs(ball.xcor())
    return x_distance_from_paddle <= THRESHOLD and ball.distance(paddle) < 50


def out_of_bounds(paddle: Paddle, ball: Ball):
    abs_paddle_x_position = abs(paddle.position()[0])
    distance_from_paddle = abs_paddle_x_position - abs(ball.xcor())
    return distance_from_paddle <= -THRESHOLD
