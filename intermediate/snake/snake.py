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

score = 0
scoret = t.Turtle()
scoret.up()
scoret.color('white')
scoret.goto(0, 370)
scoret.write(f'Score: {score}', True, 'center', ('Arial', 15, 'normal'))
scoret.hideturtle()


snake2 = snake.clone()
snake3 = snake.clone()
snake2.setpos(-20, 0)
snake3.setpos(-40, 0)
snakes = [snake, snake2, snake3]
screen.update()

gameover = False

def go(direction):

    global gameover
    global score

    if gameover == False:
        screen.tracer(0)

        for i in range(2, 0, -1):
            snakes[i].goto(snakes[i-1].pos())
        
        if direction == 'forward':
            snakes[0].forward(20)
        elif direction == 'right':
            snakes[0].right(90)
            snakes[0].forward(20)
        elif direction == 'left':
            snakes[0].left(90)
            snakes[0].forward(20)
        
        screen.update()
        time.sleep(.1)

        if snakes[0].xcor() >= 400 or snakes[0].xcor() <= -400 or snakes[0].ycor() >= 400 or snakes[0].ycor() <= -400:
            gameover = True
            got = t.Turtle()
            got.goto(0,0)
            got.color('white')
            got.write('Game Over!', True, 'center', ('Arial', 20, 'normal'))
            got.hideturtle()
            return

        go('forward')

screen.onkey(lambda: go('forward'), 'space')
screen.onkey(lambda: go('right'), 'Right')
screen.onkey(lambda: go('left'), 'Left')

screen.exitonclick()