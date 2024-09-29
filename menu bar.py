from tkinter import *

root = Tk()
root.title("menu bar")

menu_bar = Menu(root)

file_menu = Menu(menu_bar,tearoff=True)
file_menu.add_command(label="New File",command=NONE)
file_menu.add_command(label="Open")
file_menu.add_separator() # seperates different sections of the options
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As")

edit_menu = Menu(menu_bar)
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
edit_menu.add_separator()
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

menu_bar.add_cascade(label="File",menu=file_menu)
menu_bar.add_cascade(label="Edit",menu=edit_menu)
root.config(menu=menu_bar)

root.mainloop()