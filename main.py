from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("coral")
screen.title("Pong Game")
screen.tracer(0)

paddle_right = Paddle((380, 0))
paddle_left = Paddle((-380, 0))
ball = Ball()
score_board_left = ScoreBoard((-150, 250))
score_board_right = ScoreBoard((150, 250))


screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.xcor() > 350 and ball.distance(paddle_right) < 50:
        ball.x_bounce()

    if ball.xcor() < -350 and ball.distance(paddle_left) < 50:
        ball.x_bounce()

    if ball.xcor() > 380:
        score_board_left.increase_score()
        ball.reset()

    if ball.xcor() < -380:
        score_board_right.increase_score()
        ball.reset()

    if score_board_left.score == 10 or score_board_right == 10:
        game_is_on = False
        score_board_left.game_over()


screen.exitonclick()
