from tkinter import *
import tkmacosx as tkm
import pandas
import random

bgc = '#91C2AF'

window = Tk()
window.config(bg=bgc, padx=50, pady=50)
window.title('Flashcards')
window.minsize(400, 400)

words = pandas.read_csv('intermediate/flashcards/Turkish Translate .csv')
word = random.choice(words['Turkish'])

canvas = Canvas(width=800, height=526, bg=bgc, highlightthickness=0)
front = PhotoImage(file='intermediate/flashcards/card_front.png')
back = PhotoImage(file='intermediate/flashcards/card_front.png')
side = 'front'
image_item = canvas.create_image(400, 263, image=front) 
label_item = canvas.create_text(400, 150, text="Turkish", font=('Arial', 35, 'italic'), fill='black')
text_item = canvas.create_text(400, 263, text=f"{word}", font=('Arial', 40, 'bold'), fill='black')
canvas.grid(column=3, columnspan=5, row=1)

def canvas_click(event):
    global side

    if side == 'front':
        canvas.itemconfig(label_item, text='English')
        canvas.itemconfig(text_item, text=f"{words[words['Turkish'] == word]['English'].iloc[0]}")
        canvas.itemconfig(image_item, image=back)
        side = 'back'
    elif side == 'back':
        canvas.itemconfig(image_item, image=front) 
        side = 'front'
    
    return

empty = Label()
empty.config(text='', bg=bgc)
empty.grid(column=2, columnspan=5, row=2)

size=20
back = tkm.CircleButton(window, focuscolor='', activebackground='silver', bg='white', padx=90, highlightbackground=bgc, text='<', font=('Arial', 35), fg='black', borderless=1)
back.grid(column=1, row=1)

space = Label()
space.config(text='       ', bg=bgc)
space.grid(column=2, row=1)

space2 = Label()
space2.config(text='       ', bg=bgc)
space2.grid(column=8, row=1)

next = tkm.CircleButton(window, focuscolor='', activebackground='silver', bg='white', highlightbackground=bgc, text='>', font=('Arial', 35), fg='black', borderless=1)
next.grid(column=9, row=1)

wrong = tkm.CircleButton(window, focuscolor='', activebackground='#CC4D57', bg='#FF616D', highlightbackground=bgc, text='✘', font=('Arial', 35), fg='white', borderless=1)
wrong.grid(column=4, row=3)

correct = tkm.CircleButton(window, focuscolor='', activebackground='#51B175', bg='#66DE93', highlightbackground=bgc, text='✔', font=('Arial', 35), fg='white', borderless=1)
correct.grid(column=6, row=3)

canvas.bind("<Button-1>", canvas_click) 

window.mainloop()