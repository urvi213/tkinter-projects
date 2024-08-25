from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")

messagebox.showinfo("message","hi !! :3")
messagebox.showwarning("warning","this is a warning >:(")
messagebox.showerror("error","this is an error ;-;")

# these return a response
print(messagebox.askquestion("question","do you like books? ^_^")) # returns 'yes' or 'no'
print(messagebox.askokcancel("okcancel","do you want to continue ?? ^w^")) # returns a boolean
print(messagebox.askyesno("yesno","do you like music?")) # returns a boolean
print(messagebox.askretrycancel("retrycancel","retry or cancel? :P")) # returns a boolean


root.mainloop()