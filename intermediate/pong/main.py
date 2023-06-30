from turtle import Screen, Turtle
from score import Score
from line import Line
from paddles import Paddle
from ball import Ball
import random

screen = Screen()
screen.bgcolor('black')
screen.screensize(800, 800)

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

gameover = False

while gameover == False:
    ball.move()





screen.exitonclick()