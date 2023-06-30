from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.turtlesize(1, 3.5, 0)
        self.setheading(90)
        self.up()
