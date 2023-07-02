from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.up()
        self.pencolor('black')

    def state(self):
        self.score += 1