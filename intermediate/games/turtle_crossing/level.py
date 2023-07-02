from turtle import Turtle

class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.level = 1
        self.highscore = 1
        self.up()
        self.hideturtle()
        

    def start(self):
        self.clear()
        self.goto(-400, 360)
        self.write(f"Level {self.level}", True, "left", ('Courier', 23, 'normal'))
        self.goto(-400, 340)
        self.write(f"High Score: {self.highscore}", True, "left", ('Courier', 23, 'normal'))

    def levelup(self):
        self.level += 1
        if self.level > self.highscore:
            self.highscore = self.level
        self.start()

    def reset(self):
        self.level = 1
        self.start()

    def gameover(self):
        self.goto(0,0)
        self.write(f"Game Over!", True, "center", ('Courier', 23, 'normal'))