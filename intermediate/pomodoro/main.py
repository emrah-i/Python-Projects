from tkinter import *
import pygame
import time
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

bgc = '#FEF5E7'
check = '✔'

window = Tk()
window.config(bg=f'{bgc}', pady=40, padx=100)
window.title('Pomodoro Technique')
window.minsize(width=300, height=300)

pygame.mixer.init()

def beep():
     pygame.mixer.music.load(os.path.join(current_directory, 'beep-07a.mp3'))
     pygame.mixer.music.set_volume(.1) 
     pygame.mixer.music.play()

reg = (24, 60)
short = (4, 60)
long = (9, 60)
minutes, seconds = reg
score = 1
stop = False

def begin():
    global stop, type
    
    if score == 10:
            status.config(text='Long Break', fg='salmon')
    elif (score % 2) == 1:
        status.config(text='Work', fg='green')
    elif (score % 2) == 0:
            status.config(text='Break', fg='salmon')

    stop = False
    timer()

    return

def timer():
    global minutes, seconds, score, stop

    if not stop:
        if minutes >= 0 and seconds > 0 and score <= 10:
            if seconds > 0:
                seconds -= 1
            elif seconds == 0 and minutes > 0:
                minutes -= 1
            canvas.itemconfig(text_item, text=f"{minutes:02d}:{seconds:02d}")
            window.after(1000, timer)
        elif minutes == 0 and seconds == 0 and score == 9:
            minutes, seconds = long
            score += 1
            status.config(text='Long Break', fg='salmon')
            canvas.itemconfig(text_item, text=f"{minutes:02d}:{seconds:02d}")
            checks.config(text=f'{check * int(score / 2)}')
            beep()
            timer()
        elif minutes == 0 and seconds == 0 and (score % 2) == 1:
            minutes, seconds = short
            score += 1
            status.config(text='Break', fg='salmon')
            checks.config(text=f'{check * int(score / 2)}')
            beep()
            timer()
        elif minutes == 0 and seconds == 0 and (score % 2) == 0:
            minutes, seconds = reg
            score += 1
            status.config(text='Work', fg='green')
            beep()
            timer()

    if minutes == 0 and seconds == 0 and score == 10:
        stop = True
        status.config(text='Done', fg='black')
        canvas.itemconfig(text_item, text=f'00:00')
        
    return

def stop_temp():
    global stop, type

    status.config(text='Stopped', fg='silver')

    stop = True
    return

def reset_button():
    global score, minutes, seconds, stop, type

    stop = True
    time.sleep(.25)
    minutes, seconds = reg
    score = 1

    status.config(text='Timer', fg='gray')
    checks.config(text=f'{check * int(score / 2)}')
    canvas.itemconfig(text_item, text='00:00')
    return

canvas = Canvas(width=200, height=224, bg=bgc, highlightthickness=0)
tomato_img = PhotoImage(file=os.path.join(current_directory, 'tomato.png'))
canvas.create_image(100, 112, image=tomato_img)
text_item = canvas.create_text(100, 130, text='00:00', font=('Courier', 35, 'bold'), fill='white')
canvas.grid(column=2, row=2)

status = Label()
status.config(text='Timer', font=('Courier', 45, 'normal'), bg=bgc, fg='gray')
status.grid(column=2, row=1)

start = Button()
start.config(text='Start', highlightbackground=bgc, command=begin)
start.grid(column=1, row=3)

reset = Button()
reset.config(text='Reset', highlightbackground=bgc, command=reset_button)
reset.grid(column=3, row=3)

stop_button = Button()
stop_button.config(text='Stop', highlightbackground=bgc, command=stop_temp)
stop_button.grid(column=2, row=4)

checks = Label()
checks.config(text='', font=('Courier', 30, 'normal'), bg=bgc, fg='green')
checks.grid(column=2, row=3)

window.mainloop()