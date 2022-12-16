from turtle import Turtle


class Brick(Turtle):
    def __init__(self, position, color, score):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=3.5)
        self.goto(position)
        self.score = score


