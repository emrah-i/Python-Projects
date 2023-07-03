from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

bgc = 'white'

window = Tk()
window.config(bg=bgc, padx=50, pady=50)
window.title('Password Manager')
window.minsize(300, 300)

def add():
    web_entry, eu_entry, pass_entry = website.get(), email.get(), password.get()

    if web_entry == '' or eu_entry == '' or pass_entry == '':
        messagebox.showinfo(title='Error', message='You must fill in all fields.')
        return

    is_ok = messagebox.askokcancel(title='Confirm', message=f'Is this information correct:\n{web_entry}\n{eu_entry}\n{pass_entry}')

    if is_ok:
        with open('intermediate/password_manager/data.txt', mode='a') as file:
            file.write(f'\n{web_entry} | {eu_entry} | {pass_entry}')

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


canvas = Canvas(width=200, height=189, bg=bgc, highlightthickness=0)
logo = PhotoImage(file='intermediate/password_manager/logo.png')
canvas.create_image(100, 95, image=logo)
canvas.grid(column=2, row=1, sticky='EW')

website_text = Label(text='Website:', bg=bgc)
website_text.grid(column=1, row=2)

website = Entry(highlightbackground=bgc, highlightthickness=.5, width=35)
website.focus()
website.grid(column=2, columnspan=2, row=2, sticky='EW')

email_text = Label(text='Email/Username:', bg=bgc)
email_text.grid(column=1, row=3)

email = Entry(highlightbackground=bgc, highlightthickness=.5, width=35)
email.grid(column=2, columnspan=2, row=3, sticky='EW')

password_text = Label(text='Password:', bg=bgc)
password_text.grid(column=1, row=4)

password = Entry(highlightbackground=bgc, highlightthickness=.5, width=15)
password.grid(column=2, row=4, sticky='EW')

generate = Button(text="Generate Password", highlightbackground=bgc, command=generate)
generate.grid(column=3, row=4, sticky='EW')

add = Button(text='Add', highlightbackground=bgc, command=add)
add.grid(column=2, columnspan=2, row=5, sticky='EW')


window.mainloop()