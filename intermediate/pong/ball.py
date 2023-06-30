from turtle import Turtle
import random



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.pace = 5
        self.color('white')
        self.shape('circle')
        numb = random.randint(0, 100) % 2
        if numb == 0:
            numb2 = random.randint(0, 100) % 2
            if numb2 == 0:
                self.setheading(random.randint(0, 45))
            else:
                self.setheading(random.randint(300, 360))
        elif numb == 1:
            self.setheading(random.randint(120, 240))
        self.speed(0)
        self.up()
    
    def move(self):
        self.forward(self.pace)

    def bounce_y(self):
        coming = self.heading()
        going = 360 - coming
        self.setheading(going)
    
    def bounce_x(self):
        coming = self.heading()
        going = 180 - coming
        self.setheading(going)

    def reset(self):
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()
        numb = random.randint(0, 100) % 2
        if numb == 0:
            numb2 = random.randint(0, 100) % 2
            if numb2 == 0:
                self.setheading(random.randint(0, 45))
            else:
                self.setheading(random.randint(300, 360))
        elif numb == 1:
            self.setheading(random.randint(120, 240))
    
    def gameover(self, winner):
        self.hideturtle()
        self.goto(0, 0)
        self.write(f"{winner} Wins!", align='center', font=('Arial', 40, 'bold'))