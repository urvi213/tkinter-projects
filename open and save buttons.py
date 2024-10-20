from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile

def open():
    file = askopenfile(mode="r",filetypes=[('Python Files','*.py')]) # for list of filetypes give tuple (type name, extension)
    if file != None: # or if file is or if file is not
        content = file.read()
        print(content)

def save():
    file_types = [("All Files","*.*"),("Python Files","*.py"),("Text Files","*.txt")]
    asksaveasfile(filetypes=file_types,defaultextension=file_types)

root = Tk()

open_btn = Button(root,text="open",command=lambda : open())
open_btn.pack()
save_btn = Button(root,text="save",command=save)
save_btn.pack()

root.mainloop()