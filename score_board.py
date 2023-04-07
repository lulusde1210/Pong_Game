from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")


class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.ht()
        self.penup()
        self.color("white")
        self.goto(position)
        self.score = 0
        self.update_score_board()

    def increase_score(self):
        self.score += 1
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
