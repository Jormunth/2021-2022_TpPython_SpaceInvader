from tkinter import Image, PhotoImage, Tk, Label, Button, Text, StringVar, Frame, Canvas, Entry
from tkinter.constants import LEFT, RIGHT, TOP, X
from entity import Entity


class Vaisseau(Entity):

    def __init__(self, root, canvas, x1, y1, x2, y2):
        super().__init__(root,canvas,3,0,0,x1,y1,x2,y2)
        obj = self.canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2,fill="orange")
        self.setObj(obj)

    def update(self):
        self.canvas.move(self.getObj(),self.getDx(),self.getDy())
        x1,y1,x2,y2 = self.canvas.coords(self.getObj())
        w = x2-x1
        h = y2-y1
        if x1 < 0 :
            self.canvas.coords(self.getObj(),0,y1,w,y2)
        elif x2 > self.canvas.winfo_width() :
            self.canvas.coords(self.getObj(),self.canvas.winfo_width() - w,y1,self.canvas.winfo_width(),y2)
        if y1 < 0 :
            self.canvas.coords(self.getObj(),x1,0,x2,h)
        elif y2 > self.canvas.winfo_height() :
            self.canvas.coords(self.getObj(),x1,self.canvas.winfo_height() - h,x2,self.canvas.winfo_height())
        self.root.after(20,lambda : self.update())
        
class Missile(Entity):

    def __init__(self, root, canvas, x1, y1, x2, y2):
        super().__init__(root,canvas,1,0,-15,x1,y1,x2,y2)
        obj = self.canvas.create_rectangle(self.x1+15,self.y1+5,self.x2-15,self.y2-5,fill="red")
        self.setObj(obj)
    
    def update(self):
        # print(self.getDx(),self.getDy())
        self.canvas.move(self.getObj(),self.getDx(),self.getDy())
        x1,y1,x2,y2 = self.canvas.coords(self.getObj())
        if not self.inBounds() :
            self.destroy()
            return
        self.root.after(5,lambda : self.update())






