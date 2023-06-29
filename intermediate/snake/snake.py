import turtle as t
import time

screen = t.Screen()
snake = t.Turtle()
snake.shape('square')
snake.color('white')
snake.turtlesize(1, 1, 0)
snake.width(10)
snake.speed(1)
snake.up()

screen.bgcolor('black')
screen.listen()
screen.tracer(0)

snake2 = snake.clone()
snake3 = snake.clone()
snake2.setpos(-10, 0)
snake3.setpos(-20, 0)
snakes = [snake, snake2, snake3]
screen.update()

#    for i in range(2, 1, -1):
#        snakes[i].goto(snakes[i - 1].pos())


def go_forward():

    screen.tracer(0)

    snakes[0].forward(5)

    for i in range(2, 1, -1):
        snakes[i].setpos(snakes[i - 1].pos())
        snakes[i].forward(5)
    
    screen.update()
    
    go_forward()
        
def turn_right():
    snakes[0].right(90)

    for i in range(2, 1, -1):
        time.sleep(0.1)
        snakes[i].setpos(snakes[i - 1].pos())

def turn_left():
    screen.tracer(0)
    for s in snakes:
        numb = snakes.index(s)
        s.forward(5 * 5)
        s.speed(0)
        s.left(90)
        s.speed(2)
    
    screen.update()


screen.onkey(go_forward, 'space')
screen.onkey(turn_right, 'Right')
screen.onkey(turn_left, 'Left')

screen.exitonclick()