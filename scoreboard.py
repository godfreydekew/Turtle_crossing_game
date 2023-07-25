FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 1
        self.hideturtle()
        self.color("black")
        self.goto(-230, 260)
        self.write(f"level:{self.score}", align="center", font=FONT)

    def update_score(self):

        self.clear()
        self.score += 1
        self.write(f"level:{self.score}", align="center", font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)




