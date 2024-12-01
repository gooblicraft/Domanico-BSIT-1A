from tkinter import *

window = Tk(sc)
e = Entry(window, width=50, border=10)
e.pack()
e.insert(0, "Enter your name: ")

def inClick():
    mylabel1 = Label(window, text = e.get(), fg="blue",)
    mylabel1.pack()

myButton = Button(window, text="Enter your name", padx=20, command=inClick, fg="red", bg="black")
myButton.pack()

#Creating a label widget


#Shoving it onto the screen
window.mainloop()
