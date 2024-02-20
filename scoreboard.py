from turtle import Turtle
from ball import Ball

TEXT_LOCATION = (0, 180)
TEXT_COLOR = "white"
TEXT_ALIGN = "center"
FONT = ('Courier', 80, 'bold')
SMALLER_FONT = ('Courier', 12, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = [0, 0]
        self.color(TEXT_COLOR)
        self.hideturtle()
        self.print_mid_line()
        self.print_score()

    def increase_score(self, ball: Ball, amount=1):
        self.clear()
        if ball.xcor() < 0:
            self.score[0] += amount
        else:
            self.score[1] += amount
        self.print_score()
        self.print_mid_line()

    def print_mid_line(self):
        self.teleport(0, 200)
        self.seth(270)
        for _ in range(10):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def print_score(self):
        self.teleport(*TEXT_LOCATION)
        self.write(f"{self.score[0]}  {self.score[1]}", align=TEXT_ALIGN, font=FONT)

    def game_over(self):
        self.home()
        self.write("Game Over.", align=TEXT_ALIGN, font=FONT)
        self.teleport(0,-30)
        self.write(f"To try again type 'r'.", align=TEXT_ALIGN, font=SMALLER_FONT)
