from tkinter.constants import X


class Entity():
    
    def __init__(self,game,lives,dx,dy):
        self.lives = lives
        self.game = game
        self.__object = None
        self.__dx = dx
        self.__dy = dy

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

    def getWidth(self):
        x1,y1,x2,y2 = self.game.getCanvas().coords(self.getObj())
        return x2 - x1

    def getHeight(self):
        x1,y1,x2,y2 = self.game.getCanvas().coords(self.getObj())
        return y2 - y1

    def update(self):
        if self.game.getStatus() == "stopped":
            self.destroy()
        self.game.getCanvas().move(self.getObj(),self.getDx(),self.getDy())
        self.game.getRoot().after(20,lambda : self.update())

    def inBounds(self):
        if self.game.getCanvas().coords(self.getObj()) == []:
            return True
        x1,y1,x2,y2 = self.game.getCanvas().coords(self.getObj())
        if x2 < 0 or x1 > self.game.getCanvas().winfo_width() :
            print("out of bounds X")
            return False
        if y2 < 0 or y1 > self.game.getCanvas().winfo_height() :
            print("out of bounds Y")
            return False
        return True

    def destroy(self):
        self.game.getCanvas().delete(self.getObj())
        del self
    
    def removeLives(self, x):
        self.lives -= x
        print(self.lives)
        if self.lives == 0:
            self.destroy()

    # Returns true if the self is on top of an alien
    def hitbox(self,x):
        if self.game.getCanvas().coords(self.getObj()) == []:
            return False
        else:
            x1,y1,x2,y2 = self.game.getCanvas().coords(self.getObj())
       
        if self.game.getCanvas().coords(x) == []:
            return False
        else:
            a1,b1,a2,b2 = self.game.getCanvas().coords(x)
        
        if x1 < a2 and x2 > a1 and y1 < b2 and y2 > b1:
            return True
            
        

