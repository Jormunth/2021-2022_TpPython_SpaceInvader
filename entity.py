from tkinter.constants import X


class Entity():
    def __init__(self,root,canvas,lives,dx,dy,nb):
        self.lives = lives
        self.root = root
        self.canvas = canvas
        self.__object = None
        self.__dx = dx
        self.__dy = dy
        self.nb = nb

    def getnb(self):
        return self.nb 

    def setlives(self,vie):
        self.lives = vie
        
    def setObj(self,obj):
        self.__object = obj

    def getObj(self):
        if self.__object == None:
            return False
        else:
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
        s1,y1,x2,y2 = self.canvas.coords(self.getObj())
        if x2 < 0 or s1 > self.canvas.winfo_width() :
            print("out of bounds X")
            return False
        if y2 < 0 or y1 > self.canvas.winfo_height() :
            print("out of bounds Y")
            return False
        return True

    def destroy(self):
    
        print("obj destroyed")
        self.canvas.delete(self.getObj())
        del self
    
    def hitbox(self,x):

        if self.canvas.coords(self.getObj()) == []:
            return False
        else:
            z1,y1,x2,y2 = self.canvas.coords(self.getObj())
       
        if self.canvas.coords(x) == []:
            return False
        else:
            a1,b1,a2,b2 = self.canvas.coords(x)
        
        if z1 < a2 and x2 > a1 and y1 < b2 and y2 > b1:
            return True

    def tuer(self,p):
        self.canvas.delete(p)
        del self
            
        
