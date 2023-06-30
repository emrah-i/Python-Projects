import turtle as t
import random

class Food():

    def __init__(self):
        self.pos = (random.randint(-370, 370), random.randint(-370, 370))

    def start(self):

        points = t.Turtle()
        points.shape(self.shape)
        points.color(self.color)
        points.up()
        points.turtlesize(.5, .5, 0)
        points.goto(self.pos)

    def change(self):

        self.pos = (random.randint(-370, 370), random.randint(-370, 370))
