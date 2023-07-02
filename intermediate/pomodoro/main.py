from tkinter import *
import time

bgc = '#FEF5E7'
check = '✔'

window = Tk()
window.config(bg=f'{bgc}', pady=50, padx=50)
window.title('Pomodoro Technique')
window.minsize(300,300)

minutes = 24
seconds = 60
score = 0
type = 'timer'
stop = False

def begin():
    global stop
    
    if minutes == 24 and seconds == 60 and score == 0:
        status.config(text='Work', fg='green')

    stop = False
    if type == 'timer':
        timer()
    elif type == 'break':
        break_timer()

    return

def timer():
    global minutes
    global seconds
    global score
    global stop

    if stop == False:
        if minutes >= 0 and seconds > 0 and score < 5:
            if seconds > 0:
                seconds -= 1
            elif seconds == 0 and minutes > 0:
                minutes -= 1
            canvas.itemconfig(text_item, text=f"{minutes:02d}:{seconds:02d}")
            window.after(1000, timer)
        elif minutes == 0 and seconds == 0 and score < 4:
            minutes = 4
            seconds = 60
            score += 1
            status.config(text='Break', fg='salmon')
            canvas.itemconfig(text_item, text=f"{minutes:02d}:{seconds:02d}")
            checks.config(text=f'{check * score}')
            break_timer()
        elif minutes == 0 and seconds == 0 and score == 4:
            minutes = 19
            seconds = 60
            score += 1
            status.config(text='Break', fg='salmon')
            canvas.itemconfig(text_item, text=f"{minutes:02d}:{seconds:02d}")
            checks.config(text=f'{check * score}')
            break_timer()
        
    return

def break_timer():
    global minutes
    global seconds

    if stop == False:
        if minutes >= 0 and seconds > 0:
            if seconds > 0:
                seconds -= 1
            elif seconds == 0 and minutes > 0:
                minutes -= 1
            canvas.itemconfig(text_item, text=f"{minutes:02d}:{seconds:02d}")
            window.after(1000, break_timer)
        elif minutes == 0 and seconds == 0 and score < 5:
            minutes = 24
            seconds = 60
            status.config(text='Work', fg='green')
            canvas.itemconfig(text_item, text=f"{minutes:02d}:{seconds:02d}")
            timer()
        elif minutes == 0 and seconds == 0 and score == 5:
            status.config(text='Done', fg='black')
            canvas.itemconfig(text_item, text=f'00:00')
        
    return

def stop_temp():
    global stop
    global type

    if status['text'] == 'Work':
        type = 'timer'
    else: 
        type = 'break'

    stop = True
    return

def reset_button():
    global score
    global minutes
    global seconds
    global stop
    global type

    stop = True
    type = 'timer'
    time.sleep(.25)
    minutes = 24
    seconds = 60
    score = 0

    status.config(text='Timer', fg='gray')
    checks.config(text=f'{check * score}')
    canvas.itemconfig(text_item, text='00:00')
    return

canvas = Canvas(width=200, height=224, bg=bgc, highlightthickness=0)
tomato_img = PhotoImage(file='intermediate/pomodoro/tomato.png')
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