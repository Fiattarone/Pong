import time
from turtle import Screen
import paddle
import ball
import scorebrain

PLAYER_COORDS = (350, 0)
LEFT_COORDS = (-350, 0)

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

player_paddle = paddle.Paddle(PLAYER_COORDS)
left_paddle = paddle.Paddle(LEFT_COORDS)
activeBall = ball.Ball()
scoreboard = scorebrain.Scorebrain()

screen.listen()

screen.onkeypress(key="Up", fun=player_paddle.move_up)
screen.onkeypress(key="Down", fun=player_paddle.move_down)
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)

game_running = True

while game_running:
    activeBall.move()
    activeBall.check_collision(player_paddle)
    activeBall.check_collision(left_paddle)
    activeBall.check_wall_collision()
    if activeBall.check_right_goal():
        scoreboard.increase_score(num=1, str="left")
        activeBall.reset()
    elif activeBall.check_left_goal():
        scoreboard.increase_score(num=1, str="right")
        activeBall.reset()

    time.sleep(0.02)

    screen.update()

screen.exitonclick()
