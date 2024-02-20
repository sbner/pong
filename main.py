import time
from turtle import Screen
import collision
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

SCREEN_RESOLUTION = (800, 600)
SCREEN_TITLE = "Pong"
SCREEN_BG_COLOR = "black"
REFRESH_SCREEN_RATE = .04
# REFRESH_SCREEN_RATE = .1
game_over = False

# Screen Setup
screen = Screen()
screen.setup(*SCREEN_RESOLUTION)
screen.title(SCREEN_TITLE)
screen.bgcolor(SCREEN_BG_COLOR)
screen.tracer(0)

# Paddle Init
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

# Scoreboard Init
scoreboard = Scoreboard()

# Ball Init
ball = Ball()


def exit_game():
    screen.bye()


# Keybinding
def map_keys(array_of_keys):
    for key in array_of_keys:
        screen.onkeypress(key["function"], key["biding"])


key_mapping = [
    {
        "function": left_paddle.move_up,
        "biding": "w"
    },
    {
        "function": left_paddle.move_down,
        "biding": "s"
    },
    {
        "function": left_paddle.move_up,
        "biding": "W"
    },
    {
        "function": left_paddle.move_down,
        "biding": "S"
    },
    {
        "function": right_paddle.move_up,
        "biding": "Up"
    },
    {
        "function": right_paddle.move_down,
        "biding": "Down"
    },
    {
        "function": exit_game,
        "biding": "Escape"
    },
]
screen.listen()
map_keys(key_mapping)

while not game_over:
    if collision.with_wall(screen, ball):
        ball.y_bounce()
    elif collision.with_paddle(left_paddle, ball) or collision.with_paddle(right_paddle, ball):
        ball.x_bounce(increase_speed=True)
    elif collision.out_of_bounds(left_paddle, ball) or collision.out_of_bounds(right_paddle, ball):
        scoreboard.increase_score(ball)
        time.sleep(.8)
        ball.home()
    else:
        ball.move()

    # Update Screen
    time.sleep(REFRESH_SCREEN_RATE)
    screen.update()

screen.exitonclick()
