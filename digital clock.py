from tkinter import *
import tkinter.font as font
from time import strftime # this allows working with date and time as a string
import random

light_colours = ["#D1E9F6","#F6EACB","#F1D3CE","#EECAD5","#E7FBE6","#CBE2B5","#F0EAAC","#BBE9FF","#E2DAD6","#FFC6C6","#FFBB70"]
dark_colours = ["#2E073F","#7A1CAC","#1E201E","#3C3D37","#522258","#180161","#17153B","#1A3636","#0C0C0C","#352F44","#472D2D"]

def time():
    time_string = strftime("%A, %I:%M:%S %p") # hour:minute:second
    if strftime("%p") == "PM":
        time_label.config(text=time_string,fg=random.choice(light_colours),bg=random.choice(dark_colours))
    else:
        time_label.config(text=time_string,fg=random.choice(dark_colours),bg=random.choice(light_colours))
    time_label.after(1000,time) # calls time after 1000 miliseconds (1 second)

window = Tk()
window.title("clock")
window.config(bg="white")

title_label = Label(window,text="my digital clock :3")
title_label.pack()

time_label = Label(window,font=("Calibri",40,"bold"),fg="black",bg="white")
time_label.pack(anchor="s") # anchor=n, ne, e, se, s, sw, w, nw, or center

time()
window.mainloop()

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
