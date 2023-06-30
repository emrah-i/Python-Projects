from turtle import Screen, Turtle
from score import Score
from line import Line
from paddles import Paddle
from ball import Ball
import random

screen = Screen()
screen.bgcolor('black')
screen.title('Pong')

line = Line()

paddle1 = Paddle()
paddle1.goto(380, 0)

paddle2 = Paddle()
paddle2.goto(-380, 0)

score1 = Score()
score1.goto(60, 300)
score1.scoreboard()

score2 = Score()
score2.goto(-60, 300)
score2.scoreboard()

ball = Ball()

screen.listen()
screen.tracer(0)
screen.onkey(paddle1.moveup, 'Up')
screen.onkey(paddle1.movedown, 'Down')
screen.onkey(paddle2.moveup, 'w')
screen.onkey(paddle2.movedown, 's')


gameover = False 

while gameover == False:

    ball.move()
    screen.update()

    if ball.xcor() >= 360 and paddle1.distance(ball) <= 50:
        ball.bounce_x()
    elif ball.xcor() <= -360 and paddle2.distance(ball) < 50:
        ball.bounce_x()

    if ball.ycor() >= 380 or ball.ycor() <= -370:
        ball.bounce_y()
    
    if ball.xcor() >= 380:
        ball.reset()
        score2.score += 1
        score2.rewrite()
    
    if ball.xcor() <= -380:
        ball.reset()
        score1.score += 1
        score1.rewrite()

    total = score1.score + score2.score

    if total == 2:
        ball.pace = 6
    elif total == 4:
        ball.pace = 7
    elif total == 6:
        ball.pace = 8

    if score1.score == 5:
        line.gameover()
        ball.gameover("Player 1")
        gameover = True
    elif score2.score == 5:
        line.gameover()
        ball.gameover("Player 2")
        gameover = True

screen.exitonclick()