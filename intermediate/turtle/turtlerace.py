import turtle as t
import random

red = t.Turtle()
blue = t.Turtle()
green = t.Turtle()
orange = t.Turtle()
purple = t.Turtle()
black = t.Turtle()
screen = t.Screen()

turtles = [red, blue, green, orange, purple, black]

red.color('red')
blue.color('blue')
green.color('green')
orange.color('orange')
purple.color('purple')
black.color('black')

location = -330

for turt in turtles:
    turt.shape('turtle')
    turt.speed(7)
    turt.turtlesize(2, 2, 6)
    turt.up()
    turt.setx(-370)
    turt.sety(location)
    location += 130
    turt.speed(3)

winner = ''

def move_forward():

    global winner

    for turt in turtles:
        numb = random.randint(0, 20)
        turt.forward(numb)

        if turt.xcor() >= 400:
            winner = turt.pencolor() 

            if choice:
                if choice.lower().strip() == winner:
                    print(f'Congrats, you guessed right!\nThe winner is {winner}.\n')
                else:
                    print(f'You guessed wrong.\nThe winner is {winner}.\n')
            else:
                print(f'The winner is {winner}.\n')

            return
        
    move_forward()

screen.title('Welcome to Turtle Racing!')
choice = screen.textinput('Guess', 'Which color turtle do you think is going to win?')
move_forward()
screen.bye()
