from tkinter import *
from gtts import gTTS  # google text to speech (installed in command prompt)
import os # to save + play file

def play():
    language = "en" # there are dfferent codes for languaes
    audio = gTTS(text=text_entry.get(),lang=language,slow=False)
    audio.save("ttsaudio.mp3")
    os.system("ttsaudio.mp3")

root = Tk()

frame1 = Frame(root)
frame1.config(bg="pink",height=60,width=100)
frame1.pack(fill=X)
frame2 = Frame(root)
frame2.config(bg="blue",height=60,width=100)
frame2.pack(fill=X)
title_label=Label(frame1,text="Text To Speech",bg="pink")
title_label.pack()
text_entry=Entry(frame2,width=30)
text_entry.pack(padx=10,pady=10)
submit_btn = Button(frame2,bg="white",text="SUBMIT",command=play)
submit_btn.pack(padx=10,pady=10)

root.mainloop()
