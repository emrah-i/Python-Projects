from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.setheading(random.randint(0, 360))
        self.up()
    
    def move(self):
        self.forward(5)

    def rebound(self):
        coming = self.heading()
        going = 360 - coming
        self.setheading(going)