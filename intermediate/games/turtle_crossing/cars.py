from turtle import Turtle
from level import Level
import random

level = Level().level
speed = 5
amount = 6

class Cars():

    def __init__(self):
        self.cars = []


    def create(self):
        global amount

        numb = random.randint(1, amount)
        if numb == 1:
            new = Turtle()
            new.color(255, 255, 255)
            new.hideturtle()
            new.up()
            new.goto(450, random.randint(-300, 300))
            new.setheading(180)
            new.shape('square')
            new.turtlesize(1, 2, 0)
            new.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            new.showturtle()
            self.cars.append(new)

    def move(self):
        for car in self.cars:
            car.forward(speed)

    def levelup(self):
        global speed
        global amount 
        if level < 3:
            speed += 2
        elif level >= 3:
            speed += 2
            if amount > 2:
                amount -= 2
            elif amount == 2:
                amount -= 1
            else:
                amount = 1

    def reset(self):
        global speed
        global amount
        speed = 5
        amount = 6






