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

if paddle1.distance(ball) <= 15 or paddle2.distance(ball) <= 15:
    ball.rebound()

if ball.ycor() == 380 or ball.ycor() == -380:
    ball.rebound()


screen.listen()

screen.onkey(paddle1.moveup, 'Up')
screen.onkey(paddle1.movedown, 'Down')
screen.onkey(paddle2.moveup, 'w')
screen.onkey(paddle2.movedown, 's')

ball.move()

screen.exitonclick()