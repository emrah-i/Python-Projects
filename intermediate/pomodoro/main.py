from tkinter import *

bgc = '#FEF5E7'
check = '✔'

window = Tk()
window.config(bg=f'{bgc}', pady=50, padx=50)
window.title('Pomodoro Technique')
window.minsize(300,300)

minutes = 0
seconds = 3
score = 0

def timer():
    global minutes
    global seconds
    global score

    if minutes >= 0 and seconds > 0 and score < 5:
        if seconds > 0:
            seconds -= 1
        elif seconds == 0 and minutes > 0:
            minutes -= 1
        canvas.itemconfig(text_item, text=f'{minutes}:{seconds}')
        window.after(1000, timer)
    elif minutes == 0 and seconds == 0 and score < 5:
        minutes = 4
        seconds = 60
        score += 1
        canvas.itemconfig(text_item, text=f'{minutes}:{seconds}')
        checks.config(text=f'{check * score}')
        break_timer()
        
    return

def break_timer():
    global minutes
    global seconds

    if minutes >= 0 and seconds > 0:
        if seconds > 0:
            seconds -= 1
        elif seconds == 0 and minutes > 0:
            minutes -= 1
        canvas.itemconfig(text_item, text=f'{minutes}:{seconds}')
        window.after(1000, break_timer)
    elif minutes == 0 and seconds == 0:
        minutes = 24
        seconds = 60
        timer()

    break_timer()

def reset():
    canvas.itemconfig(text_item, text='00:00')


canvas = Canvas(width=200, height=224, bg=bgc, highlightthickness=0)
tomato_img = PhotoImage(file='intermediate/pomodoro/tomato.png')
canvas.create_image(100, 112, image=tomato_img)
text_item = canvas.create_text(100, 130, text='00:00', font=('Courier', 35, 'bold'), fill='white')
canvas.grid(column=2, row=2)

status = Label()
status.config(text='Work', font=('Courier', 45, 'normal'), bg=bgc)
status.grid(column=2, row=1)

start = Button()
start.config(text='Start', highlightbackground=bgc, command=timer)
start.grid(column=1, row=3)

reset = Button()
reset.config(text='Reset', highlightbackground=bgc, command=reset)
reset.grid(column=3, row=3)

checks = Label()
checks.config(text='', font=('Courier', 30, 'normal'), bg=bgc, fg='green')
checks.grid(column=2, row=3)

window.mainloop()