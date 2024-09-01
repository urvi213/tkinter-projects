from tkinter import *
import tkinter.font as font
from tkinter import messagebox
import random

random_num = random.randint(1,20)

def check():
    if num_entry.get().isdigit() == False:
        messagebox.showinfo("invalid input msg","invalid input :(")
    elif int(num_entry.get()) > random_num:
            messagebox.showinfo("too high msg","your guess was too high TwT")
    elif int(num_entry.get()) < random_num:
         messagebox.showinfo("too low","your guess was too low ;-;")
    else:
         messagebox.showinfo("correct msg","your guess was correct !!! :D")

window = Tk()
window.config(background="white")
window.title("guess my number :3")

num_entry = Entry(window,font=font.Font(size=15))
num_entry.pack(pady=10)

submit_btn = Button(window,text="submit",font=font.Font(size=15),bg="pink",command=check)
submit_btn.pack(pady=10)

messagebox.showinfo("start msg","i'm thinking of a number between 1 and 20. can you guess it ?? >:3")

window.mainloop()