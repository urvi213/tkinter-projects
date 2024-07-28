from tkinter import *

root = Tk()
root.title("login")
root.geometry("500x400")
root.configure(background="pink")

# creating label
user_name = Label(root,text="username",fg="purple",bg="lightblue").place(x=40,y=60) # fg means foreground colour (font colour)
user_password = Label(root,text="password",fg="purple",bg="lightblue").place(x=40,y=100)

submit_btn = Button(root,text="submit",background="white",bd="5").place(x=40,y=140)

#input areas
un_input_area = Entry(root,width=30).place(x=120,y=60)
pw_input_area = Entry(root,width=30,show="*").place(x=120,y=100) # show="*" displays typed characters as *

root.mainloop()