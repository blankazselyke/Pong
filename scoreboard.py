from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.draw_scoreboard()

    def draw_scoreboard(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Agency FB", 50, "normal"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Agency FB", 50, "normal"))

    def r_scored(self):
        self.r_score += 1
        self.draw_scoreboard()

    def l_scored(self):
        self.l_score += 1
        self.draw_scoreboard()

    def game_over(self):
        return self.r_score == 10 or self.l_score == 10

    def win(self):
        self.draw_scoreboard()
        x_pos = 0
        if self.l_score == 10:
            x_pos = -200
        else:
            x_pos = 200
        self.goto(x_pos, 50)
        self.write("WIN", align="center", font=("Agency FB", 50, "normal"))