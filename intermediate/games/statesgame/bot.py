from turtle import Turtle

class Bot(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.speed(0)
        self.pencolor('black')

    def state(self, x, y, state):
        self.goto(x, y)
        self.write(f'{state}', True, 'left', ('Arial', 7, 'normal'))