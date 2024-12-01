from tkinter import *
from tkinter import font
from tkinter import messagebox
import random

score = 0
total = 0

def run():
    global answer
    score_label.config(text="score = {}/{}".format(score,total))
    entry.delete(0,END)
    answer=random.choice(words)
    shuffled_answer= list(answer)
    random.shuffle(shuffled_answer)
    word_label.config(text=shuffled_answer)

def check():
    global score, total
    answer_input = entry.get()
    if answer_input.strip() == "": messagebox.showerror("no input","enter an answer")
    else:
        if answer_input == answer:
            messagebox.showinfo("correct","that was correct! +1 point")
            score += 1
        else: messagebox.showinfo("incorrect","that was incorrect!\n(the correct answer was {})".format(answer))
        total += 1
        run()

def reset():
    global score,total
    score=0
    total=0
    run()

def hint():
    if random.randint(1,2) == 1: messagebox.showinfo("hint","the word starts with {}".format(list(answer)[0]))
    else: messagebox.showinfo("hint","the word ends with {}".format(list(answer)[len(list(answer))-1]))


words = ["print","hello","teacher","beach","life","death","famous","prophet","star","waiting","room","smoke","signals","punish","garden","marry","night","shift","pretend","sometimes","motif","complete","human","inhuman","control","brain","reaction","impossible","possible","gravity"]

root =Tk()

title_label = Label (root,text="jumbled word game :3",font=font.Font(size=20))
title_label.grid(row=0,pady=5,padx=5)
word_label = Label(root,font=font.Font(size=15))
word_label.grid(row=1,pady=5,padx=5)
entry = Entry(root)
entry.grid(row=2,padx=5,pady=5)
check_btn = Button(root,text="check",font=font.Font(size=15),command=check)
check_btn.grid(row=3,padx=5,pady=5)
reset_btn = Button(root,text="reset",font=font.Font(size=15),command=reset)
reset_btn.grid(row=4,padx=5,pady=5)
skip_btn = Button(root,text="skip word",font=font.Font(size=15),command=run)
skip_btn.grid(row=5,padx=5,pady=5)
hint_btn = Button(root,text="hint",font=font.Font(size=15),command=hint)
hint_btn.grid(row=6,padx=5,pady=5)
score_label = Label(root,font=font.Font(size=10))
score_label.grid(row=7,padx=5,pady=5)

run()
root.mainloop()
