from turtle import Turtle, Screen
from bot import Bot
from score import Score
import pandas

screen = Screen()
screen.bgpic("intermediate/statesgame/blank_states_img.gif")
screen.setup(725, 491)

data = pandas.read_csv("intermediate/statesgame/50_states.csv")

bot = Bot()

score = Score()
points = 0

while points < 50:
    points = score.score
    guess = screen.textinput(f'Points: {points}/50', 'Name a state:')

    if guess:
        for row in data['state']:
            if guess.lower().strip() == row.lower():
                score.state()
                x = data.loc[data['state'] == row, 'x'].iloc[0]
                y = data.loc[data['state'] == row, 'y'].iloc[0]
                bot.state(x, y, row)


screen.exitonclick()