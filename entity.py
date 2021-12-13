from tkinter.constants import X


class Entity():
    def __init__(self,canvas,lives,dx,dy):
        self.__lives = lives
        self.canvas = canvas
        self.__object = None
        self.__dx = dx
        self.__dy = dy
        
       
    def move(self):
        self.canvas.move(self.__object,self.__dx,self.__dy)

    def addObj():
        pass