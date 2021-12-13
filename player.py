from tkinter import Image, PhotoImage, Tk, Label, Button, Text, StringVar, Frame, Canvas, Entry
from tkinter.constants import LEFT, RIGHT, TOP
from entity import Entity

class Player(Entity):

    def __init__(self, canvas,lives):
        super().__init__(canvas,lives,0,0)
        self.__score=0
        self.__