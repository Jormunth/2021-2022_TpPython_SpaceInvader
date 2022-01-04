from tkinter import Image, PhotoImage, Tk, Label, Button, Text, StringVar, Frame, Canvas, Entry
from tkinter.constants import LEFT, RIGHT, TOP, X
from entity import Entity


class Vaisseau(Entity):

    def __init__(self, canvas, x1, y1, x2, y2):
        super().__init__(canvas,3,0,0,x1,y1,x2,y2)
        self.truc = self.canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2,fill="orange")
        self.setObj(self.truc)
        
    


class Missile(Entity):

    def __init__(self, canvas, x1, y1, x2, y2):
        super().__init__(canvas,0,0,-30,x1,y1,x2,y2)
        self.truc2 = self.canvas.create_rectangle(self.x1+15,self.y1+5,self.x2-15,self.y2-5,fill="red")
        self.setObj(self.truc2)   
    







