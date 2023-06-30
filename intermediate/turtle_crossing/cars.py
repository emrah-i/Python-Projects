from turtle import Turtle
import random

class Cars():

    def __init__(self):
        self.cars = []


    def create(self):
        new = Turtle()
        new.color(255, 255, 255)
        new.hideturtle()
        new.up()
        new.goto(450, random.randint(-320, 320))
        new.setheading(180)
        new.shape('square')
        new.turtlesize(1, 2, 0)
        new.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        new.showturtle()
        self.cars.append(new)

    def create(self):
        self.cars.speed(.6)
        self.cars.forward(1000)




