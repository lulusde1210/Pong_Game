from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.color("white")

    def up(self):
        if self.ycor() <= 230:
            self.sety(self.ycor()+10)

    def down(self):
        if self.ycor() >= -230:
            self.sety(self.ycor()-10)
