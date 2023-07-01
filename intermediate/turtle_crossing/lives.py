from turtle import Turtle

class Lives(Turtle):

    def __init__(self):
        super().__init__()
        self.lives = 3
        self.shape('turtle')
        self.color('black')
        self.shapesize(1.25, 1.25)
        self.speed(0)
        self.up()
        self.hideturtle()

    def start(self):
        self.goto(300, 360)
        self.write(f"Lives:", True, "left", ('Courier', 23, 'normal'))

        self.goto(290, 340)
        for _ in range(self.lives):
            self.setheading(0)
            self.forward(25)
            self.setheading(90)
            self.stamp()

    def hit(self):
        self.lives -= 1
        self.clear()
        self.start()
