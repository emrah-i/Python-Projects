from tkinter import *
import tkmacosx as tkm
import pandas
import random
import json

bgc = '#91C2AF'

window = Tk()
window.config(bg=bgc, padx=50, pady=50)
window.title('Flashcards')
window.minsize(400, 400)

side = 'front'
words = pandas.read_csv('intermediate/flashcards/Turkish Translate .csv')
word = random.choice(words['Turkish'])
try:
    with open('intermediate/flashcards/learned.json') as file:
        try:
            data = json.load(file)
        except:
            learned_words = []
        else:
            learned_words = [word for word in data]
except FileNotFoundError:
    learned_words = []

def missed():
    global side
    global word

    word = random.choice(words['Turkish'])
    while word in learned_words:
        word = random.choice(words['Turkish'])

    side = 'front'
    canvas.itemconfig(label_item, text='Turkish', fill='black')
    canvas.itemconfig(text_item, text=f"{word}", fill='black')
    canvas.itemconfig(image_item, image=front_img)

def learned():
    global side
    global word
    global learned_words

    learned_words.append(word)
    adding = word

    word = random.choice(words['Turkish'])
    while word in learned_words:
        word = random.choice(words['Turkish'])
        
    side = 'front'
    canvas.itemconfig(label_item, text='Turkish', fill='black')
    canvas.itemconfig(text_item, text=f"{word}", fill='black')
    canvas.itemconfig(image_item, image=front_img)

    try:
        with open('intermediate/flashcards/learned.json') as file:
            try:
                data = json.load(file)
            except:
                with open('intermediate/flashcards/learned.json', mode='w') as file:
                    json.dump(learned_words, file)
            else:
                data.append(adding)
                with open('intermediate/flashcards/learned.json', mode='w') as file:
                    json.dump(data, file)
    except FileNotFoundError:
        with open('intermediate/flashcards/learned.json', mode='w') as file:
            json.dump(learned_words, file)

def canvas_click(event):
    global side

    if side == 'front':
        canvas.itemconfig(label_item, text='English', fill='white')
        canvas.itemconfig(text_item, text=f"{words[words['Turkish'] == word]['English'].iloc[0]}",  fill='white')
        canvas.itemconfig(image_item, image=back_img) 
        side = 'back'
    elif side == 'back':
        canvas.itemconfig(label_item, text='Turkish', fill='black')
        canvas.itemconfig(text_item, text=f"{word}", fill='black')
        canvas.itemconfig(image_item, image=front_img) 
        side = 'front'
    
    return

canvas = Canvas(width=700, height=446, bg=bgc, highlightthickness=0)
front_img = PhotoImage(file='intermediate/flashcards/front_img.png')
back_img = PhotoImage(file='intermediate/flashcards/back_img.png')
image_item = canvas.create_image(350, 223, image=front_img) 
label_item = canvas.create_text(350, 180, text="Turkish", font=('Arial', 30, 'italic'), fill='black')
text_item = canvas.create_text(350, 250, text=f"{word}", font=('Arial', 35, 'bold'), fill='black')
canvas.grid(column=2, columnspan=3, row=1)
canvas.bind("<Button-1>", canvas_click) 

size=20
wrong = tkm.CircleButton(window, focuscolor='', activebackground='#CC4D57', bg='#FF616D', highlightbackground=bgc, text='✘', font=('Arial', 35), fg='white', borderless=1, command=missed)
wrong.grid(column=2, row=3)

correct = tkm.CircleButton(window, focuscolor='', activebackground='#51B175', bg='#66DE93', highlightbackground=bgc, text='✔', font=('Arial', 35), fg='white', borderless=1, command=learned)
correct.grid(column=4, row=3)

window.mainloop()