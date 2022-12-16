import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def collision(self, obstacle):
        ball_width = 5
        half_width = ball_width + (obstacle.shapesize()[1] / 2) * 20
        half_height = ball_width + (obstacle.shapesize()[0] / 2) * 20
        if obstacle.xcor() + half_width >= self.xcor() >= obstacle.xcor() - half_width and obstacle.ycor() - half_height <= self.ycor() <= obstacle.ycor() + half_height:
            return True

    def reset_position(self):
        x_position = random.randint(-390, 390)
        self.goto(x_position, 0)
        self.bounce_x()
