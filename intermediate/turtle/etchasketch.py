import turtle as t

bob = t.Turtle()
screen = t.Screen()
screen.listen()

def move_forwards():
    bob.forward(10)

def turn_left():
    bob.left(10)

def turn_right():
    bob.right(10)

def move_backwards():
    bob.backward(10)

screen.onkey(move_forwards, 'Up')
screen.onkey(turn_left, 'Left')
screen.onkey(turn_right, 'Right')
screen.onkey(move_backwards, 'Down')
screen.exitonclick()
