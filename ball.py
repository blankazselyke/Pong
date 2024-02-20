from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_dir = 1
        self.y_dir = 1
        self.velocity = 1

    def move(self, x, y):
        x = x * self.velocity
        y = y * self.velocity
        if 290 > self.ycor() > - 290:
            self.goto(self.xcor() + x * self.x_dir, self.ycor() + y * self.y_dir)
        elif self.ycor() >= 290:
            self.y_dir = -1
            self.goto(self.xcor() + x * self.x_dir, self.ycor() + y * self.y_dir)
        elif self.ycor() <= -290:
            self.y_dir = 1
            self.goto(self.xcor() + x * self.x_dir, self.ycor() + y * self.y_dir)

    def bounce(self):
        if self.xcor() * self.x_dir > 0:
            self.x_dir = self.x_dir * -1
            self.velocity += 0.3


    def reset(self):
        self.goto(0, 0)
        self.x_dir = self.x_dir * -1
        self.velocity = 1
