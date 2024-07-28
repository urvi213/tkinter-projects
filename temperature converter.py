from tkinter import *
import tkinter.font as font

root = Tk()
root.geometry("600x600")
root.configure(background="white")
root.title("temperature converter")

def show_conversion():
    fahrenheit_temp = float(temperature_entry.get())
    fahrenheit_temp = str(fahrenheit_temp*1.8+32)
    f_label.configure(text=fahrenheit_temp)

title_label = Label(root,text="temperature converter",fg="black",bg="white",font=font.Font(size=20))
title_label.grid(row=2,column=0,columnspan=2)

entry_label = Label(root,text="enter temperature in Celsius:",fg="black",bg="white",font=font.Font(size=10))
entry_label.grid(row=3,column=0)

temperature_entry = Entry(root,width=40)
temperature_entry.grid(row=3,column=1)

convert_btn = Button(root,text="convert to Fahrenheit",background="pink",bd=1,command=show_conversion,font=font.Font(size=10))
convert_btn.grid(row=4,column=0)
f_label = Label(root,text="label",fg="black",bg="white")
f_label.grid(row=5,column=0)

root.mainloop()