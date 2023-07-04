from tkinter import *
import tkmacosx as tkm
import random

bgc = '#FFEAC9'

window = Tk()
window.config(bg=bgc, padx=50, pady=50)
window.title('Flashcards')
window.minsize(400, 400)

canvas = Canvas(width=800, height=526, bg='white', highlightthickness=0)
canvas.grid(column=1, columnspan=5, row=1)

empty = Label()
empty.config(text='', bg=bgc)
empty.grid(column=1, columnspan=5, row=2)

size = 20
wrong = tkm.CircleButton(window, focuscolor='', activebackground='#CC4D57', bg='#FF616D', highlightbackground=bgc, pady=size, text='X', font=('Chalkboard', 35, 'bold'), fg='white', borderless=1)
wrong.grid(column=2, row=3)

correct = tkm.CircleButton(window, focuscolor='', activebackground='#51B175', bg='#66DE93', highlightbackground=bgc, pady=size, text='✔', font=('Arial', 35), fg='white', borderless=1)
correct.grid(column=4, row=3)

window.mainloop()