from tkinter import Image, PhotoImage, Tk, Label, Button, Text, StringVar, Frame, Canvas, Entry
from tkinter.constants import LEFT, RIGHT, TOP, X
from entity import Entity


class Player(Entity):

    def __init__(self, canvas,x,y):
        super().__init__(canvas,3,0,0)
        self.__score=0
        self.x = x
        self.y = y
        self.__object = self.canvas.create_rectangle(self.x, self.y, self.x+10, self.y+10,fill="green")
