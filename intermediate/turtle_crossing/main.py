from turtle import Screen
from cars import Cars
from user import User
from level import Level
from lines import Lines

screen = Screen()
screen.title('Road Crossing')
screen.colormode(255)

user = User()

cars = Cars()

lines = Lines()
lines.start()
lines.end()

screen.listen()
screen.onkey(user.go, 'Up')
screen.onkey(user.right, 'Right')
screen.onkey(user.left, 'Left')
screen.onkey(user.back, 'Down')

gameover = False

def start():

    global gameover

    while gameover == False:

            cars.send()


screen.onkey(start, 'space')
screen.exitonclick()