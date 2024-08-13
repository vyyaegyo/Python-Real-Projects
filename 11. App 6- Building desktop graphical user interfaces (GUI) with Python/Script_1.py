from tkinter import *

window = Tk()

e1_values=StringVar()
e1 = Entry(window, textvariable=e1_values)
e1.grid(row=0, column=1)

def km_to_miles():
    miles=float(e1_values.get())*1.6
    t1.insert(END,miles)

b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0, column=0)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()