import turtle as t

class Snake:

    def __init__(self):
        self.segments = []

    def create(self):

        snake = t.Turtle()
        snake.shape('square')
        snake.color('white')
        snake.turtlesize(1, 1, 0)
        snake.width(10)
        snake.speed(1)
        snake.up()

        snake2 = snake.clone()
        snake3 = snake.clone()
        snake2.setpos(-20, 0)
        snake3.setpos(-40, 0)
        
        self.segments += [snake, snake2, snake3]
    
    def move(self, direction):

        for i in range(2, 0, -1):
            self.segments[i].goto(self.segments[i-1].pos())
        
        if direction == 'forward':
            self.segments[0].forward(20)
        elif direction == 'right':
            self.segments[0].right(90)
            self.segments[0].forward(20)
        elif direction == 'left':
            self.segments[0].left(90)
            self.segments[0].forward(20)

    def gameover(self):

        got = t.Turtle()
        got.goto(0,0)
        got.color('white')
        got.write('Game Over!', True, 'center', ('Arial', 20, 'normal'))
        got.hideturtle()