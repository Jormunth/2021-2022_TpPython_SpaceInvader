from tkinter import Image, PhotoImage, Tk, Label, Button, Text, StringVar, Frame, Canvas, Entry
from tkinter.constants import LEFT, RIGHT, TOP, X
from entity import Entity


class Player(Entity):
    def __init__(self, canvas, lives):
        super().__init__(canvas,lives,0,-30)


class Vaisseau(Player):

    def __init__(self, canvas,):
        super().__init__(canvas,3)
        self.setObj(self.canvas.create_rectangle(390, 390, 410, 410,fill="orange"))
    

class Missile(Player):

    def __init__(self, canvas):
        super().__init__(canvas,0)
        self.setObj(self.canvas.create_rectangle(395, 395, 405, 410,fill="orange"))   
        



