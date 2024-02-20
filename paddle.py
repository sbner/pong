from turtle import Turtle

PADDLE_COLOR = "white"
PADDLE_SHAPE = "square"
PADDLE_SIZE = (5, 1)
MOVE_DISTANCE = 15


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(PADDLE_SHAPE)
        self.teleport_paddle(position)
        self.paddle_setup()
        self.speed(0)

    def paddle_setup(self):
        self.penup()
        self.color(PADDLE_COLOR)
        self.turtlesize(*PADDLE_SIZE)
        self.speed(0)

    def teleport_paddle(self, position: (int, int)):
        self.teleport(*position)

    def move_up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        self.sety(self.ycor() - MOVE_DISTANCE)

    # def position(self):
    #     return self.xcor(), self.ycor()
