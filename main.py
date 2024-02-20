from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from square import Square
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
for i in range(0, 20):
    square = Square((0, -280 + 30 * i))

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_over = False
while not game_over:
    time.sleep(0.001)
    screen.update()
    #scoreboard.draw_scoreboard()
    #ball.move(0.4, 0.3)
    ball.move(0.5, 1)
    if ball.distance(r_paddle) < 50 and 350 > ball.xcor() > 330:
        ball.bounce()
    elif ball.distance(l_paddle) < 50 and -350 < ball.xcor() < -330:
        ball.bounce()
    elif ball.xcor() > 420:
        time.sleep(0.5)
        ball.reset()
        r_paddle.reset()
        l_paddle.reset()
        scoreboard.l_scored()
        time.sleep(1)
    elif ball.xcor() < -420:
        time.sleep(0.5)
        ball.reset()
        r_paddle.reset()
        l_paddle.reset()
        scoreboard.r_scored()
        time.sleep(1)
    game_over = scoreboard.game_over()

scoreboard.win()
screen.update()
screen.exitonclick()
