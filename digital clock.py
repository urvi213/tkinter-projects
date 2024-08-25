from tkinter import *
import tkinter.font as font
from time import strftime # this allows working with date and time as a string

def time():
    time_string = strftime("%A, %I:%M:%S %p") # hour:minute:second
    time_label.config(text=time_string)
    time_label.after(1000,time) # calls time after 1000 miliseconds (1 second)

window = Tk()
window.title("clock")
window.config(bg="white")

time_label = Label(window,font=("Calibri",40,"bold"),fg="black",bg="white")
time_label.pack(anchor="s") # anchor=n, ne, e, se, s, sw, w, nw, or center

time()
window.mainloop()

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior