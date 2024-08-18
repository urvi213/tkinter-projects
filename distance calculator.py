from tkinter import *
import tkinter.font as font

def calculate():
    speed = speed_entry.get()
    time = time_entry.get()
    if speed.replace(".","",1).isdigit() and time.replace(".","",1).isdigit():
        output_label.config(text=str(int(speed)*int(time)))
        error_label.config(text="")
    else:
        output_label.config(text="")
        error_label.config(text="invaild input(s)")

root = Tk()
root.configure(background="white")
root.title("distance calculator")

frame = Frame()
frame.pack(padx=30,pady=30)

title_label = Label(frame,text="calculate distance",font=font.Font(size=30))
title_label.grid(row=0,column=0,columnspan=2)

speed_entry_label = Label(frame,text="enter speed in km/hr",font=font.Font(size=15))
speed_entry_label.grid(row=1,column=0)
speed_entry = Entry(frame)
speed_entry.grid(row=1,column=1)

time_entry_label = Label(frame,text="enter time in hrs",font=font.Font(size=15))
time_entry_label.grid(row=2,column=0)
time_entry = Entry(frame)
time_entry.grid(row=2,column=1)

output_title_label = Label(frame,text="distance in km:",font=font.Font(size=15))
output_title_label.grid(row=3,column=0)
output_label = Label(frame)
output_label.grid(row=3,column=1)

calculator_btn = Button(frame,text="calculate",background="pink",font=font.Font(size=20),command=calculate)
calculator_btn.grid(row=4,column=0,columnspan=2)

error_label = Label(frame,text="",fg="red",font=font.Font(size=15))
error_label.grid(row=5,column=0,columnspan=2)

root.mainloop()