from turtle import Screen
from paddle import Paddle
from ball import Ball
from Bricks import Brick
import time
from scoreboard import Scoreboard

Wall = []
x_positions = [-40, -120, -200, -280, -360, 40, 120, 200, 280, 360]
y_positions = [230, 200, 170, 140]
colors = ["green", "blue", "red", "yellow"]


def setup():
    for block in Wall:
        block.reset()
    Wall.clear()
    i = 0
    for y in y_positions:
        for x in x_positions:
            Wall.append(Brick((x, y), colors[i], 5 - i))
        i += 1


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)
scoreboard = Scoreboard()

paddle = Paddle((0, -250))

ball = Ball()
ball.reset_position()
setup()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")
previous_score = 0
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() <= -390 or ball.xcor() >= 390:
        ball.bounce_x()

    if ball.ycor() >= 290:
        ball.bounce_y()

    if ball.collision(paddle):
        ball.bounce_y()
    for brick in Wall:
        if ball.collision(brick):
            scoreboard.point(brick.score)
            brick.reset()
            Wall.remove(brick)
            ball.bounce_y()

    if ball.ycor() < -290:
        scoreboard.game_status(screen, "OVER")
        setup()
        scoreboard.update_scoreboard()
        ball.reset_position()

    if (previous_score // 5) < (scoreboard.score // 5):
        ball.move_speed *= 0.95
        previous_score = scoreboard.score

    if len(Wall) == 0:
        scoreboard.game_status(screen, "WON")
        setup()
        scoreboard.update_scoreboard()
        ball.reset_position()

screen.exitonclick()
