from turtle import Turtle


class Square(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")

        # width = 20, height = 100
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.goto(position)
