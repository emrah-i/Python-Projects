import turtle as t
import time
import random
from snake import Snake

screen = t.Screen()
screen.bgcolor('black')
screen.title('My Snake Game')
screen.listen()
screen.tracer(0)

snake = Snake()
snake.create()
screen.update()

gameover = False

def go(direction):

    global gameover

    if gameover == False:
        screen.tracer(0)

        snake.move(direction)
        
        screen.update()
        time.sleep(.1)

        if snake.segments[0].xcor() >= 400 or snake.segments[0].xcor() <= -400 or snake.segments[0].ycor() >= 400 or snake.segments[0].ycor() <= -400:
            gameover = True
            snake.gameover()
            return

        go('forward')


screen.onkey(lambda: snake.move('forward'), 'space')
screen.onkey(lambda: snake.move('right'), 'Right')
screen.onkey(lambda: snake.move('left'), 'Left')

screen.exitonclick()