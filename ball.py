# from math import sqrt
from random import choice
from turtle import Turtle

BALL_SHAPE = "circle"
BALL_COLOR = "white"
INITIAL_MOVE_STEP = 5


class Ball(Turtle):
    def __init__(self):
        super().__init__(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.penup()
        self.move_x_step = INITIAL_MOVE_STEP
        self.move_y_step = INITIAL_MOVE_STEP
        # self.move_x_step = 0
        # self.move_y_step = 0
        # self.set_random_heading()

    def move(self):
        current_x = self.xcor() + self.move_x_step
        current_y = self.ycor() + self.move_y_step
        self.goto(current_x, current_y)

    def y_bounce(self):
        self.move_y_step *= -1
        self.move()

    def x_bounce(self, increase_speed=False, increase_rate=1.1, reset_speed=False):
        self.move_x_step *= -1

        if increase_speed:
            self.move_x_step *= increase_rate
            self.move_y_step *= increase_rate
        elif reset_speed:
            self.move_x_step = INITIAL_MOVE_STEP
            self.move_y_step = INITIAL_MOVE_STEP

        self.move()

    def home(self):
        super().home()
        # self.set_random_heading()
        self.move_y_step *= choice([-1, 1])
        self.x_bounce(reset_speed=True)

    # def set_random_heading(self):
    #     random_number = random() * MOVE_STEP * choice([-1, 1])
    #     self.move_y_step = random_number
    #     self.move_x_step = sqrt(sqrt(50) - random_number**2)
