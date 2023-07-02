from tkinter import *

window = Tk()
window.title("Miles to km")
window.minsize(300, 150)
window.config(bg='aliceblue', padx=30, pady=30)

def convert_miles():
    numb = int(miles.get())
    numb_convert = round((numb * 1.6093), 2)
    km.config(text=f'{numb_convert}')
    return

miles = Entry(width=8, highlightbackground='aliceblue')
miles.grid(column=2, row=1)

m_label = Label(text='miles', font=('Arial', 15, 'normal'), bg='aliceblue')
m_label.grid(column=3, row=1)

km = Label(text='0', font=('Arial', 15, 'normal'), bg='aliceblue')
km.grid(column=2, row=2)

km_label = Label(text='kilometers', font=('Arial', 15, 'normal'), bg='aliceblue')
km_label.grid(column=3, row=2)

m_to_km_label = Label(text='is equal to:', font=('Arial', 15, 'normal'), bg='aliceblue')
m_to_km_label.grid(column=1, row=2)

convert = Button(text='calculate', command=convert_miles, highlightbackground='aliceblue')
convert.grid(column=2, row=3)



window.mainloop()