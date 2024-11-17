from tkinter import *
import speech_recognition as sr
from tkinter.filedialog import asksaveasfile

def rec():
    recogniser = sr.Recognizer() # creates an object
    with sr.Microphone() as source:
        print("speak")
        audio = recogniser.listen(source)
        try:
            text = recogniser.recognize_google(audio)
        except:
            text="didnt recognise"
        rec_text.delete(1.0,END)
        rec_text.insert(END,text)

def save():
    user_file = asksaveasfile(defaultextension="*.txt")    
    if user_file != None:
        print(rec_text.get(1.0,END),file=user_file)

root = Tk()

title_label = Label(root,text="voice notepad")
title_label.grid(column=0,columnspan=3,row=0,padx=10,pady=10)
rec_btn = Button(root,text="click on me! \nto start recording",command=rec)
rec_btn.grid(column=0,row=1,padx=10,pady=10)
rec_text =Text(root,height=5)
rec_text.grid(row=1,column=1,padx=10,pady=10)
save_btn = Button(root,text="save the text",command=save)
save_btn.grid(row=1,column=2,padx=10,pady=10)

root.mainloop()