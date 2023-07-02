from turtle import Turtle

class Lines(Turtle):

    def __init__(self):
        super().__init__()
        self.pensize(5)
        self.pencolor('black')
        self.hideturtle()
        self.up()

    def start(self):
        self.speed('fastest')
        self.goto(410, -320)
        self.seth(180)
        self.down()
        for _ in range(40):
            self.forward(20)
            self.up()
            self.forward(20)
            self.down()
        self.up()
    
    def end(self):
        self.speed('fastest')
        self.goto(410, 320)
        self.seth(180)
        self.down()
        for _ in range(40):
            self.forward(20)
            self.up()
            self.forward(20)
            self.down()
        self.up()
