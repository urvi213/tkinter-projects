from tkinter import *
from tkinter import messagebox as mb
import speech_recognition as sr

name = ""
fav_food = ""

def rec_food():
    global fav_food, name
    recogniser = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recogniser.listen(source)
        try: 
            fav_food = recogniser.recognize_google(audio)
            if fav_food.strip() != "" and name.strip() != "":
                mb.showinfo("message","hi {}, i love {} !! :3".format(name,fav_food))
        except: 
            mb.showerror("error","speech not recognised")

def rec_name():
    global fav_food, name
    recogniser = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recogniser.listen(source)
        try: 
            name = recogniser.recognize_google(audio)
            if fav_food.strip() != "" and name.strip() != "":
                mb.showinfo("message","hi {}, i love {} !! :3".format(name,fav_food))
        except: 
            mb.showerror("error","speech not recognised")

root = Tk()

name_btn = Button(root,text="click to record your name",command=rec_name)
name_btn.grid(row=0,column=0,padx=10,pady=10)
food_btn = Button(root,text="click to record your favourite food",command=rec_food)
food_btn.grid(row=0,column=1,padx=10,pady=10)

root.mainloop()