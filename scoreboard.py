import time
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(350, 230)
        if self.score >= 100:
            font_size = 40
        else:
            font_size = 50
            self.write(self.score, align="center", font=("Courier", font_size, "normal"))

    def point(self, point):
        self.score += point
        self.update_scoreboard()

    def game_status(self, screen,status):
        for i in range(6):
            screen.update()
            self.clear()
            self.goto(0, 0)
            self.write(f"GAME {status} Your Score is:{self.score}\n Game will reset in:{5-i} seconds", align="center",
                       font=("Courier", 20, "normal"))
            time.sleep(1)
        self.score = 0


