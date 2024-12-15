from tkinter import *
import time

WIDTH = 900
HEIGHT = 700

root = Tk()
root.resizable(width=False,height=False) # can no longer change size
bg = Canvas(root,bg="black",width=WIDTH,height=HEIGHT)
bg.pack()
bg.create_line(WIDTH/2,0,WIDTH/2,HEIGHT,fill="white",width=1)
bg.create_oval(WIDTH/2-50,HEIGHT/2-50,WIDTH/2+50,HEIGHT/2+50,outline="white",width=1)
bg.create_text(WIDTH/2,30,text=":",font=("Arial",20,"bold"),fill="pink")

class L_Paddle(object):

    COLOUR = "yellow"

    def __init__(self):
        self.rect = bg.create_rectangle(0,HEIGHT/2-60,15,HEIGHT/2+60,fill=self.COLOUR)
        self.yChange = 0
        bg.bind_all("w",self.up) # bind() binds to one specfic widget, bind_all() runs no matter what widget is in focus
        bg.bind_all("s",self.down)

    def up(self,event):
        print("up")
        self.yChange = -2.5

    def down(self,event):
        print("down")
        self.yChange = 2.5

    def draw(self):
        #print("draw")
        bg.move(self.rect,0,self.yChange)
        pos = bg.coords(self.rect)
        if pos[1] <= 0 or pos[3] >= HEIGHT:
            self.yChange = -self.yChange

lPaddle = L_Paddle()
root.update()

while True:
   lPaddle.draw()
   root.update()
   time.sleep(0.01)

root.mainloop()