from tkinter import *

bgc = 'white'

window = Tk()
window.config(bg=bgc, padx=50, pady=50)
window.title('Password Manager')
window.minsize(300, 300)

canvas = Canvas(width=200, height=189, bg=bgc, highlightthickness=0)
logo = PhotoImage(file='intermediate/password+manager/logo.png')
canvas.create_image(100, 95, image=logo)
canvas.grid(column=2, row=1, sticky='EW')

website_text = Label(text='Website:', bg=bgc)
website_text.grid(column=1, row=2)

website = Entry(highlightbackground=bgc, highlightthickness=1 ,width=35)
website.grid(column=2, columnspan=2, row=2, sticky='EW')

email_text = Label(text='Email/Username:', bg=bgc)
email_text.grid(column=1, row=3)

email = Entry(highlightbackground=bgc, highlightthickness=1, width=35)
email.grid(column=2, columnspan=2, row=3, sticky='EW')

password_text = Label(text='Password:', bg=bgc)
password_text.grid(column=1, row=4)

password = Entry(highlightbackground=bgc, highlightthickness=1, width=15)
password.grid(column=2, row=4, sticky='EW')

generate = Button(text="Generate Password", highlightbackground=bgc)
generate.grid(column=3, row=4, sticky='EW')

add = Button(text='Add', highlightbackground=bgc)
add.grid(column=2, columnspan=2, row=5, sticky='EW')


window.mainloop()