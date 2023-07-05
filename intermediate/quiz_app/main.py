from tkinter import *
from tkinter import messagebox
from random import choice
from time import sleep
import tkmacosx as tkm
import requests
import html

bgc = '#AED6F1'

window = Tk()
window.config(bg=bgc, padx=50, pady=50)
window.title('Quiz App')
window.minsize(350, 350)

response = requests.get(url='https://opentdb.com/api_token.php?command=request')
data = response.json()
st = data['token']
response = requests.get(url=f'https://opentdb.com/api.php?amount=50&category=9&type=boolean&token={st}')
data = response.json()
data = data['results']
total = len(data)

question = choice(data)
already_done = []

score = 0

def guess(answer):
    global score
    global question

    if question['correct_answer'] == answer:
        canvas.config(bg='#5D9C59')
        score += 1
        sl.config(text=f'Score: {score}')
    else:
        canvas.config(bg='#DF2E38')

    window.update()
    sleep(.7)
    canvas.config(bg='white')
    already_done.append(question)

    if len(already_done) == total:
        messagebox.showinfo(title='Done', message='You finished all of the question!')
        return
    
    question = choice(data)
    while question in already_done:
        question = choice(data)

    canvas.itemconfig(item_diff, text=f"Difficulty: {question['difficulty']}")
    canvas.itemconfig(item_text, text=f"{html.unescape(question['question'])}")
    return

sl = Label()
sl.config(text=f'Score: {score}', font=('Arial', 20, 'bold'), bg=bgc)
sl.grid(column=2, columnspan=2, row=1)

canvas = Canvas(width=300, height=400, bg='white', highlightbackground=bgc)
item_diff = canvas.create_text(150, 70, text=f"Difficulty: {question['difficulty']}", fill='black', width=260, font=('Arial', 20, 'bold'))
item_text = canvas.create_text(150, 150, text=f"{html.unescape(question['question'])}", fill='black', width=260, font=('Arial', 20))
canvas.grid(column=1, columnspan=4, row=2)

space = Label(text=" ", fg=bgc, bg=bgc)
space.grid(column=1, columnspan=4, row=3)

tb = tkm.CircleButton()
tb.config(bg='#DF2E38', text='✘', font=('Arial', 24), fg='white', borderless=1, activebackground='#B2242C', focuscolor='', command=lambda: guess('True'))
tb.grid(column=1, row=4)

fb = tkm.CircleButton()
fb.config(bg='#5D9C59', text='✔', font=('Arial', 24), fg='white', borderless=1, activebackground='#4A7C47', focuscolor='', command=lambda: guess('False'))
fb.grid(column=4, row=4)

window.mainloop()