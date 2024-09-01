from tkinter import *

root = Tk()
root.geometry=("500x300")
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

list = Listbox(root,yscrollcommand=scrollbar.set)

for i in range(30):
    list.insert(END,str(i))

list.pack(fill=BOTH) # fill=BOTH means list fills both x and y
scrollbar.config(command=list.yview)

root.mainloop()