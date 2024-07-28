from tkinter import *
import calendar

def show_calendar():
    calendar_window = Tk()
    calendar_window.title("{} calendar".format(year_input.get()))
    calendar_window.configure(background="pink")
    calendar_window.geometry("600x800")
    year = int(year_input.get())
    calendar_text = calendar.month(year,2)
    calendar_label = Label(calendar_window,text=calendar_text)
    calendar_label.grid(row=0,column=0)

    calendar_window.mainloop()

root = Tk() # window
root.title("entry page")
root.configure(background="white")
root.geometry("500x500")


title_label = Label(root,text="CALENDAR",fg="black",bg="white")
title_label.grid(row=0,columnspan=2,column=2)

year_label = Label(root,text="year?",fg="black",bg="white")
year_label.grid(row=3,column=0)

year_input = Entry(root,width=20)
year_input.grid(row=3,column=1)

submit_btn = Button(root,text="submit",background="pink",bd=5,command=show_calendar)
submit_btn.grid(row=6,columnspan=5)

root.mainloop()