from tkinter import *
root = Tk() # creates window
root.geometry('200x400') # width and height

btn = Button(root,text="Click Me :3",bd="6",background="pink",command=root.destroy)
btn.pack(side="right") # you can use bottom, left, right, top

root.mainloop()