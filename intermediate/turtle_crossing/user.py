from turtle import Turtle

class User(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.shapesize(1.25, 1.25)
        self.up()
        self.seth(90)
        self.speed(0)
        self.goto(0, -350)
    
    def go(self):
        self.setheading(90)
        self.forward(20)
    
    def right(self):
        self.setheading(0)
        self.forward(20)
    
    def left(self):
        self.setheading(180)
        self.forward(20)
    
    def back(self):
        self.setheading(270)
        self.forward(20)
