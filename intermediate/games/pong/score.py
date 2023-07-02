from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.up()
    
    def scoreboard(self):
        self.write(f"{self.score}", align='center', font=('Arial', 80, 'bold'))

    def rewrite(self):
        self.clear()
        self.write(f"{self.score}", align='center', font=('Arial', 80, 'bold'))
