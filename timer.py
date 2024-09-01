from tkinter import *
from tkinter import font
from tkinter import messagebox
import time

root = Tk()
root.title("timer")
#root.geometry("130x100")

hours = StringVar()
minutes = StringVar()
seconds = StringVar()

def reset():
    hours.set("00")
    minutes.set("00")
    seconds.set("00")

def start():
    try:
        total_seconds = int(hours.get())*3600+int(minutes.get())*60+int(seconds.get())
    except:
        messagebox.showerror("incorrect value","enter a correct value")

    while total_seconds >= 0:
        m, s = divmod(total_seconds,60) 
        h=0
        if m > 60:
            h,m = divmod(m,60)
        hours.set("{:02d}".format(h)) # puta 0 in empty space, be 2 digits, d stands for digits
        minutes.set("{:02d}".format(m))
        seconds.set("{:02d}".format(s))
        root.update()
        time.sleep(1)
        total_seconds -= 1

reset()

hours_entry = Entry(root,width=30,textvariable=hours)
hours_entry.place(x=10,y=10)

minutes_entry = Entry(root,width=30,textvariable=minutes)
minutes_entry.place(x=50,y=10)

seconds_entry = Entry(root,width=30,textvariable=seconds)
seconds_entry.place(x=90,y=10)

start_btn = Button(root,text="start timer !",bg="pink",font=font.Font(size=15),width=30,command=start)
start_btn.place(x=15,y=30)

root.mainloop()
