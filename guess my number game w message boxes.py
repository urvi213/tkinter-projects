from tkinter import *
import tkinter.font as font
from tkinter import messagebox
import random

random_num = random.randint(1,20)

def start():
     messagebox.showinfo("start msg","i'm thinking of a number between 1 and 20. can you guess it ?? >:3")
     start_frame.pack_forget()
     game_frame.pack()

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

start_frame = Frame(window)

welcome_label = Label(start_frame,text="welcome to my game !! ^_^")
welcome_label.pack(pady=10)
start_btn = Button(start_frame,text="start !!",command=start)
start_btn.pack(pady=10)

start_frame.pack()

game_frame = Frame(window)

num_entry = Entry(game_frame,font=font.Font(size=15))
num_entry.pack(pady=10)

submit_btn = Button(game_frame,text="submit",font=font.Font(size=15),bg="pink",command=check)
submit_btn.pack(pady=10)

window.mainloop()
