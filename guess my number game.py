from tkinter import *
import tkinter.font as font
import random

random_num = random.randint(1,20)

def check():
    if num_entry.get().isdigit() == False:
        result_label.config(text="invalid input ;-;")
    elif int(num_entry.get()) > random_num:
            result_label.config(text="your guess is too high TwT")
    elif int(num_entry.get()) < random_num:
         result_label.config(text="your guess is too low TwT")
    else:
         result_label.config(text="congratulations! you are right :D")

window = Tk()
window.config(background="white")
window.title("guess my number :3")

title_label = Label(window,text="guess my number (it is between 1 and 20) :3",font=font.Font(size=20),bg="white")
title_label.pack(padx=10,pady=10)

num_entry = Entry(window,font=font.Font(size=15))
num_entry.pack(pady=10)

submit_btn = Button(window,text="submit",font=font.Font(size=15),bg="pink",command=check)
submit_btn.pack(pady=10)

result_label = Label(window,text="^w^",font=font.Font(size=20),fg="darkred",bg="white")
result_label.pack()

window.mainloop()