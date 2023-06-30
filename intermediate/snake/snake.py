from turtle import Turtle

class Snake:

    def __init__(self):
        self.segments = []

        snake = Turtle()
        snake.shape('square')
        snake.color('white')
        snake.turtlesize(1, 1, 0)
        snake.width(5)
        snake.speed(1)
        snake.up()

        snake2 = snake.clone()
        snake3 = snake.clone()
        snake2.setpos(-20, 0)
        snake3.setpos(-40, 0)
        
        self.segments += [snake, snake2, snake3]
        self.head = self.segments[0]
    
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i-1].pos())
        
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def add(self):
        segment = self.head.clone()
        segment.goto(self.segments[-1].pos())
        self.segments.append(segment)

    def gameover(self):

        got = Turtle()
        got.goto(0,0)
        got.color('white')
        got.write('Game Over!', True, 'center', ('Arial', 20, 'normal'))
        got.hideturtle()