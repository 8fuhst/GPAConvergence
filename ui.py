from tkinter import *
from SchnittKonv import Calculator

# Initialize Frame
root = Tk()

c = Calculator()

current_average = Label(root, text="Your current average: " + c.get_current_average())

current_average.pack()

root.mainloop()

def add_row():
    