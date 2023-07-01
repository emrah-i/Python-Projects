from turtle import Screen
from cars import Cars
from user import User
from level import Level
from lines import Lines
from lives import Lives
import time

screen = Screen()
screen.title('Road Crossing')
screen.colormode(255)

user = User()

cars = Cars()

lines = Lines()
lines.start()
lines.end()

lives = Lives()
lives.start()

level = Level() 

with open("intermediate/turtle_crossing/hs.txt") as file:
    contents = int(file.read())
    level.highscore = contents

level.start()

screen.listen()
screen.tracer(0)
screen.onkey(user.go, 'Up')
screen.onkey(user.right, 'Right')
screen.onkey(user.left, 'Left')
screen.onkey(user.back, 'Down')

gameover = False

while gameover == False:

        screen.update()
        cars.create()
        time.sleep(.05)
        cars.move()

        if user.ycor() >= 320:
            user.reset()
            level.levelup()
            cars.levelup()
        
        for i in range(len(cars.cars)):
            if user.distance(cars.cars[i]) <= 30:
                user.reset()
                level.reset()
                cars.reset()
                lives.hit()
                with open("intermediate/turtle_crossing/hs.txt", mode='w') as file:
                    if level.highscore > contents:
                        file.write(str(level.highscore))
                    else:
                        file.write(str(contents))

                if lives.lives == 0:
                    gameover = True
                    user.hideturtle()
                    level.gameover()
                

        if user.xcor() <= -390 or user.xcor() >= 390 or user.ycor() <= -400:
            user.reset()


screen.exitonclick()