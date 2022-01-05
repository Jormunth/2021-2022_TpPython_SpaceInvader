from tkinter.constants import X


class Entity():
    def __init__(self,root,canvas,lives,dx,dy,X1,Y1,X2,Y2):
        self.__lives = lives
        self.root = root
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

    def update(self):
        self.canvas.move(self.getObj(),self.getDx(),self.getDy())
        self.root.after(20,lambda : self.update())

    def inBounds(self):
        x1,y1,x2,y2 = self.canvas.coords(self.getObj())
        if x2 < 0 or x1 > self.canvas.winfo_width() :
            print("out of bounds X")
            return False
        if y2 < 0 or y1 > self.canvas.winfo_height() :
            print("out of bounds Y")
            return False
        return True

    def destroy(self):
        x1,y1,x2,y2 = self.canvas.coords(self.getObj())
        print(x1,y1,x2,y2)
        print("obj destroyed")
        self.canvas.delete(self.getObj())
        del self