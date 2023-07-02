from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.turtlesize(1, 5, 0)
        self.setheading(90)
        self.speed(7)
        self.up()

    def moveup(self):
        self.forward(50)
    
    def movedown(self):
        self.backward(50)
    
