from tkinter import *
from tkinter import ttk
import time

def progress():
    progress_bar["value"] = 20
    root.update_idletasks()
    time.sleep(1)
    progress_bar["value"] = 40
    root.update_idletasks()
    time.sleep(1)
    progress_bar["value"] = 60
    root.update_idletasks()
    time.sleep(1)
    progress_bar["value"] = 80
    root.update_idletasks()
    time.sleep(1)
    progress_bar["value"] = 100
    root.update_idletasks()

root = Tk()
root.title("progress bar")

progress_bar = ttk.Progressbar(root,orient=HORIZONTAL,mode="determinate")
progress_bar.pack()
btn = Button(root,text="progress",command=progress)
btn.pack()

root.mainloop()