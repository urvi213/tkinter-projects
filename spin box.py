from tkinter import *

root = Tk()
root.title("Spin Box")

spin_box = Spinbox(root,from_=1,to=20)
spin_box.pack()

root.mainloop()