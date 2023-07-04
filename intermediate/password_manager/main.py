from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

bgc = '#FEF5E7'

window = Tk()
window.config(bg=bgc, padx=50, pady=50)
window.title('Password Manager')
window.minsize(300, 300)

win = Toplevel(bg=bgc, padx=25, pady=25)
win.minsize(150, 150)
win.title('Information')
win.withdraw()
message = Label(win, font=('Arial', 15, 'normal'), bg=bgc, pady=30)
message.grid(column=2, row=1)
copy_pass = Button(win, text='Copy Password', width=10, highlightbackground=bgc)
copy_pass.grid(column=1, row=2)
copy_email = Button(win, text='Copy User', width=10, highlightbackground=bgc)
copy_email.grid(column=2, row=2)
close = Button(win, text='Close', width=10, highlightbackground=bgc)
close.grid(column=3, row=2)

def add():
    web_entry, eu_entry, pass_entry = website.get(), email.get(), password.get()
    new_entry = {
        web_entry: {
            'email': eu_entry,
            'password': pass_entry
        }
    }
    if web_entry == '' or eu_entry == '' or pass_entry == '':
        messagebox.showinfo(title='Error', message='You must fill in all fields.')
        return

    is_ok = messagebox.askokcancel(title='Confirm', message=f'Is this information correct:\n{web_entry}\n{eu_entry}\n{pass_entry}')

    if is_ok:
        with open('intermediate/password_manager/data.json', mode='r') as file:
            data = json.load(file)
            data.update(new_entry)

        with open('intermediate/password_manager/data.json', mode='w') as file:
            json.dump(data, file, indent=4)
        
        website.delete(0, END)
        email.delete(0, END)
        password.delete(0, END)

    return

def generate():

    random_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGIHJKLMNOPQRSTUVWXYZ'
    random_symbols = '~`!@#$%^&*()_-+={[}]|\:;<>'
    random_number = '1234567890'

    gen_pass = [choice(random_letters) for _ in range(randint(8, 10))] + [choice(random_symbols) for _ in range(randint(2, 4))] + [choice(random_number) for _ in range(randint(2, 4))]

    shuffle(gen_pass)
    gen_pass = ''.join(gen_pass)
    pyperclip.copy(gen_pass)
    password.delete(0, END)
    password.insert(0, gen_pass)

def search():
    web_search = website.get().strip()

    if web_search == '':
        messagebox.showinfo(title='Error', message='Must enter text to search')
        return
    
    try:
        with open('intermediate/password_manager/data.json', 'r') as file:
            data = json.load(file)
            try:
                entry = data[web_search]
            except KeyError:
                messagebox.showinfo(title='Error', message='No entry found under that website. Check whether text is correctely capitalized')
            else:
                win.deiconify()
                message.config(text=f"Website: {web_search}\nUser: {entry['email']}\nPassword: {entry['password']}")
                copy_pass.config(command=lambda: pyperclip.copy(entry['password']))
                copy_email.config(command=lambda: pyperclip.copy(entry['email']))
                close.config(command=lambda: win.withdraw())
    except FileNotFoundError:
        messagebox.showerror(title='No File', message='A password file does not exist. You must first create a password entry.')
            
    return

def clear_inputs():
    aus = messagebox.askyesno(title='Clear', message='Are you sure you want to clear all fields?')

    if aus == True:
        website.delete(0, END)
        email.delete(0, END)
        password.delete(0, END)
    
    return

canvas = Canvas(width=200, height=189, bg=bgc, highlightthickness=0)
logo = PhotoImage(file='intermediate/password_manager/logo.png')
canvas.create_image(100, 95, image=logo)
canvas.grid(column=2, row=1, sticky='EW')

website_text = Label(text='Website:', bg=bgc)
website_text.grid(column=1, row=2)

search = Button(text="Search", highlightbackground=bgc, command=search)
search.grid(column=3, row=2, sticky='EW')

website = Entry(highlightbackground=bgc, highlightthickness=.5)
website.focus()
website.grid(column=2, row=2, sticky='EW')

email_text = Label(text='Email/Username:', bg=bgc)
email_text.grid(column=1, row=3)

email = Entry(highlightbackground=bgc, highlightthickness=.5)
email.grid(column=2, columnspan=2, row=3, sticky='EW')

password_text = Label(text='Password:', bg=bgc)
password_text.grid(column=1, row=4)

password = Entry(highlightbackground=bgc, highlightthickness=.5)
password.grid(column=2, row=4, sticky='EW')

generate = Button(text="Generate Password", highlightbackground=bgc, command=generate)
generate.grid(column=3, row=4, sticky='EW')

add = Button(text='Add', highlightbackground=bgc, command=add)
add.grid(column=2, row=5, sticky='EW')

clear = Button(text='Clear', highlightbackground=bgc, command=clear_inputs)
clear.grid(column=3, row=5, sticky='EW')

space = Label(text='', bg=bgc)
space.grid(column=1, columnspan=3, row=6, sticky='EW')

window.mainloop()