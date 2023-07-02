import tkinter

window = tkinter.Tk()
window.title("Miles to km")
window['bg'] = 'white'
window.minsize(400, 400)

my_label = tkinter.Label(text='Enter miles: ', font=('Arial', 23, 'bold'))
my_label['bg'] = 'white'
my_label.pack(expand=1)




window.mainloop()