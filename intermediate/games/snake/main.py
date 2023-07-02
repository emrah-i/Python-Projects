from turtle import Screen
import time
import random
from snake import Snake
from scoreboard import Score
from food import Food

screen = Screen()
screen.bgcolor('black')
screen.title('My Snake Game')
screen.listen()
screen.tracer(0)

snake = Snake()
screen.update()

score = Score()
score.start()

food = Food()

gameover = False

def go():

    global gameover

    while gameover == False:

        snake.move()

        screen.update()
        time.sleep(.08)

        if snake.head.distance(food) < 20:
            score.update()
            food.move()
            snake.add()
        
        for i in range(len(snake.segments)):
            if i > 0:
                if snake.head.distance(snake.segments[i]) < 15:
                    gameover = True
                    snake.gameover()
                    return

        if snake.head.xcor() >= 400 or snake.head.xcor() <= -400 or snake.head.ycor() >= 400 or snake.head.ycor() <= -400:
            gameover = True
            snake.gameover()
            return

screen.onkey(go, 'space')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

screen.exitonclick()