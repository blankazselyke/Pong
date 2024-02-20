from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from square import Square
import time


class Game():
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.title("Pong")
        self.screen.tracer(0)

        self.r_paddle = Paddle((350, 0))
        self.l_paddle = Paddle((-350, 0))
        self.ball = Ball()
        self.scoreboard = Scoreboard()
        for i in range(0, 20):
            square = Square((0, -280 + 30 * i))

        self.screen.listen()
        self.screen.onkeypress(self.r_paddle.go_up, "Up")
        self.screen.onkeypress(self.r_paddle.go_down, "Down")
        self.screen.onkeypress(self.l_paddle.go_up, "w")
        self.screen.onkeypress(self.l_paddle.go_down, "s")
        self.screen.onkeypress(self.restart, "Return")

    def play(self):
        game_over = False
        while not game_over:
            time.sleep(0.001)
            self.screen.update()
            self.ball.move(0.5, 1)
            if self.ball.distance(self.r_paddle) < 50 and 350 > self.ball.xcor() > 330:
                self.ball.bounce()
            elif self.ball.distance(self.l_paddle) < 50 and -350 < self.ball.xcor() < -330:
                self.ball.bounce()
            elif self.ball.xcor() > 420:
                self.ball.reset()
                # r_paddle.reset()
                # l_paddle.reset()
                self.scoreboard.l_scored()
            elif self.ball.xcor() < -420:
                self.ball.reset()
                # r_paddle.reset()
                # l_paddle.reset()
                self.scoreboard.r_scored()
            game_over = self.scoreboard.game_over()
        self.scoreboard.win()
        self.screen.update()
        self.screen.exitonclick()

    def restart(self):
        if self.scoreboard.game_over():
            self.screen.clear()
            self.__init__()
            self.play()
