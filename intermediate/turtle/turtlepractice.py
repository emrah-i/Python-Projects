import turtle as t
import random
import colorgram

jim = t.Turtle()

def square():
    for _ in range(4):
        jim.forward(100)
        jim.left(90)


def dashed():
    for _ in range(15):
        jim.forward(10)
        jim.up()
        jim.forward(10)
        jim.down()


def shapes():
    jim.color('red')
    for _ in range(3):
        jim.forward(100)
        jim.right(120)

    jim.color('blue')
    for _ in range(4):
        jim.forward(100)
        jim.right(90)

    jim.color('coral')
    for _ in range(5):
        jim.forward(100)
        jim.right(72)

    jim.color('orange')
    for _ in range(6):
        jim.forward(100)
        jim.right(60)

    jim.color('green')
    for _ in range(7):
        jim.forward(100)
        jim.right(51.43)

    jim.color('purple')
    for _ in range(8):
        jim.forward(100)
        jim.right(45)

    jim.color('maroon')
    for _ in range(9):
        jim.forward(100)
        jim.right(40)

    jim.color('silver')
    for _ in range(10):
        jim.forward(100)
        jim.right(36)


def random_dir():
    jim.width(15)
    jim.speed(10)

    colors = ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "orange", "purple", "red", "silver", "teal", "coral"]

    for _ in range(100):
        numb = random.randint(1, 1000)
        rand = numb % 2
        jim.color(random.choice(colors))

        if rand == 0:
            jim.left(90)
            jim.forward(25)
        elif rand == 1: 
            jim.right(90)
            jim.forward(25)

t.colormode(255)
jim.shape('circle')

def spirograph():
    def random_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        random_color = (r, g, b)
        return random_color

    jim.speed(0)

    for _ in range(50):
        jim.color(random_color())
        jim.circle(100)
        jim.left(7.2)


def starry():
    colors = colorgram.extract('intermediate/turtle/starry_night.jpg', 30)

    rgb = []

    for i in range(len(colors)):
        rgb.append((colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b))

    jim.hideturtle()
    jim.speed(9)
    jim.up()
    jim.backward(300)
    jim.right(90)
    jim.forward(300)
    jim.left(90)
    jim.down()


    for _ in range(13):
        for _ in range(10):
            jim.dot(20, random.choice(rgb))
            jim.up()
            jim.forward(40)

        jim.left(90)
        jim.forward(40)
        jim.left(90)
        jim.forward(400)
        jim.right(180)
    
starry()

screen = t.Screen()
screen.exitonclick()
