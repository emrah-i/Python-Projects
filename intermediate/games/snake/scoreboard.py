from turtle import Turtle

scoret = Turtle()

class Score:

    def __init__(self):
        self.score = 0
    
    def start(self):
        
        scoret.up()
        scoret.color('white')
        scoret.goto(0, 370)
        scoret.write(f'Score: {self.score}', True, 'center', ('Arial', 20, 'normal'))
        scoret.hideturtle()

    def update(self):

        self.score += 1
        scoret.clear()
        scoret.goto(0, 370)
        scoret.write(f'Score: {self.score}', True, 'center', ('Arial', 20, 'normal'))
        scoret.hideturtle()