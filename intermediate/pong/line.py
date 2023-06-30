from turtle import Turtle

class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.up()
        self.goto(0, -500)
        self.speed(0)
        self.color('white')
        self.shape('square')
        self.turtlesize(0.25, 1.25, 0)
        self.setheading(90)
        self.draw()

    def draw(self):
        for _ in range(32):
            self.stamp()
            self.forward(40)