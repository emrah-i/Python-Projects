from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.up()
        self.turtlesize(.5, .5, 0)
        self.goto(random.randint(-370, 370), random.randint(-370, 370))

    def move(self):

        self.goto(random.randint(-370, 370), random.randint(-370, 370))
