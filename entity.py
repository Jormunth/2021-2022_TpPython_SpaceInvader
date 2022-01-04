from tkinter.constants import X


class Entity():
    def __init__(self,canvas,lives,dx,dy,X1,Y1,X2,Y2):
        self.__lives = lives
        self.canvas = canvas
        self.__object = None
        self.__dx = dx
        self.__dy = dy
        self.x1 = X1
        self.y1 = Y1
        self.x2 = X2
        self.y2 = Y2
        
    def setObj(self,obj):
        self.__object = obj

    def getObj(self):
        return self.__object

    def getDx(self):
        return self.__dx

    def getDy(self):
        return self.__dy

    def setDx(self,x):
        self.__dx = x

    def setDy(self,y):
        self.__dy = y