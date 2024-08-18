from tkinter import *
import tkinter.font as font
import random

options = ["rock","paper","scissors"]
user_score=0
computer_score=0

def play(user_input):
    global user_score, computer_score
    
    computer_input = random.choice(options)
    message = ""

    user_selection.config(text="you selected: {}".format(user_input))
    computer_selection.config(text="computer selected: {}".format(computer_input))
    if computer_input == user_input:
        message = "tie !"
    elif (user_input=="rock" and computer_input=="scissors") or (user_input=="paper" and computer_input=="rock") or (user_input=="scissors" and computer_input=="paper"):
        message="you win !"
        user_score += 1
    else:
        message="you lose !"
        computer_score += 1

    win_lose.config(text=message)
    user_score_msg.config(text="your score: {} ".format(user_score))
    computer_score_msg.config(text="computer score: {} ".format(computer_score))


window = Tk()
window.config(background="white")
window.title("rock paper scissors !!")

title = Label(window,text="Rock, Paper, Scissors !!",font=font.Font(size=25),bg="white",fg="darkgrey")
title.pack(padx=10,pady=10)
win_lose = Label(window,text="choose an option !",font=font.Font(size=15),bg="white",fg="darkgrey")
win_lose.pack(padx=10,pady=5)

frame = Frame(window)
frame.pack(padx=30,pady=10)

rock_btn = Button(frame,text="rock",font=font.Font(size=15),bg="pink",command=lambda: play(options[0]))
rock_btn.grid(row=0,column=0,padx=10,pady=10)
paper_btn = Button(frame,text="paper",font=font.Font(size=15),bg="yellow",command=lambda: play(options[1]))
paper_btn.grid(row=0,column=1,padx=10,pady=10)
scissors_btn = Button(frame,text="scissors",font=font.Font(size=15),bg="blue",fg="white",command=lambda: play(options[2]))
scissors_btn.grid(row=0,column=2,padx=10,pady=10)

score_frame = Frame(window)
score_frame.pack(padx=30,pady=10)

user_selection = Label(score_frame,text="you selected: - ",font=font.Font(size=15))
user_selection.grid(row=0,column=0,padx=10,pady=10)
computer_selection = Label(score_frame,text="computer selected: - ",font=font.Font(size=15))
computer_selection.grid(row=1,column=0,padx=10,pady=10)

user_score_msg = Label(score_frame,text="your score: - ",font=font.Font(size=15))
user_score_msg.grid(row=0,column=1,padx=10,pady=10)
computer_score_msg = Label(score_frame,text="computer's score: - ",font=font.Font(size=15))
computer_score_msg.grid(row=1,column=1,padx=10,pady=10)

window.mainloop()

