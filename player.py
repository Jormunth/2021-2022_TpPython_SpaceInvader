from tkinter import Image, PhotoImage, Tk, Label, Button, Text, StringVar, Frame, Canvas, Entry
from tkinter.constants import LEFT, RIGHT, TOP, X
from entity import Entity
from alien import AlienWeak


class Vaisseau(Entity):

    def __init__(self, root, canvas, x1, y1, x2, y2):
        super().__init__(root,canvas,3,0,0,x1,y1,x2,y2,0)
        obj = self.canvas.create_rectangle(self.x1,self.y1,self.x2+40,self.y2+40,fill="orange")
        self.setObj(obj)
        

    def update(self):
        self.canvas.move(self.getObj(),self.getDx(),self.getDy())
        x1,y1,x2,y2 = self.canvas.coords(self.getObj())
        if x1 < 0 :
            self.canvas.coords(self.getObj(),0,y1,40,y2)
        elif x2 > self.canvas.winfo_width() :
            self.canvas.coords(self.getObj(),760,y1,800,y2)
        if y1 < 0 :
            self.canvas.coords(self.getObj(),x1,0,x2,40)
        if y2 > self.canvas.winfo_height() :
            self.canvas.coords(self.getObj(),x1,460,x2,500)

        
        self.root.after(20,lambda : self.update())
        
class Missile(Entity):

    def __init__(self, root, canvas, x1, y1, x2, y2,EV):
        super().__init__(root,canvas,1,0,-10,x1,y1,x2,y2,EV)
        obj = self.canvas.create_rectangle(self.x1+17,self.y1+5,self.x2-17,self.y2-5,fill="red")
        self.setObj(obj)
        self.EV = EV
        
    def update(self):
        self.canvas.move(self.getObj(),self.getDx(),self.getDy())

        for i in self.EV:

            if self.hitbox(i) == True:
                self.destroy()
                self.tuer(i)
                return 

        if not self.inBounds():
            self.destroy()
            return

        self.root.after(5,lambda : self.update())



