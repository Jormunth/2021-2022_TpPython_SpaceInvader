from entity import Entity
from tkinter import Canvas

class Alien(Entity):
    def __init__(self, canvas, lives):
        super().__init__(canvas,lives,1,0)

class AlienWeak(Alien):
    def __init__(self, canvas):
        super().__init__(canvas,3)
        self.__object = self.canvas.create_rectangle(0, 0, 10, 10,fill="orange")
        """self.__object.after(1000,self.move)"""

class AlienStrong(Alien):
    def __init__(self, canvas):
        super().__init__(canvas,10)
        self.__object = self.canvas.create_rectangle(0, 0, 10, 10,fill="red")

