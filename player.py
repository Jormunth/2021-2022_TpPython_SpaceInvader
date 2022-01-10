from tkinter import Image, PhotoImage, Tk, Label, Button, Text, StringVar, Frame, Canvas, Entry
from tkinter.constants import LEFT, RIGHT, TOP, X
from entity import Entity



class Vaisseau(Entity):

    def __init__(self, game, x, y):
        super().__init__(game,3,0,0)
        obj = self.game.getCanvas().create_rectangle(x,y,x+40,y+40,fill="orange")
        self.setObj(obj)
        
    def update(self):
        canvas = self.game.getCanvas()
        canvas.move(self.getObj(),self.getDx(),self.getDy())
        x1,y1,x2,y2 = canvas.coords(self.getObj())
        if x1 < 0 :
            canvas.coords(self.getObj(),0,y1,40,y2)
        elif x2 > canvas.winfo_width() :
            canvas.coords(self.getObj(),760,y1,800,y2)
        if y1 < 0 :
            canvas.coords(self.getObj(),x1,0,x2,40)
        if y2 > canvas.winfo_height() :
            canvas.coords(self.getObj(),x1,460,x2,500)

        
        self.game.getRoot().after(20,lambda : self.update())
        
    def destroy(self):
        print("obj destroyed")
        # game.gameOver()
        self.game.getCanvas().delete(self.getObj())
        del self

class Missile(Entity):

    def __init__(self,game,x,y):
        super().__init__(game,1,x,y)

class MissileVaisseau(Missile):

    def __init__(self, game, x, y):
        super().__init__(game,0,-10)
        obj = self.game.getCanvas().create_rectangle(x+23,y+17,x-3+20,y-17,fill="red")
        self.setObj(obj)
        
    def update(self):
        print(self.getDy())
        self.game.getCanvas().move(self.getObj(),self.getDx(),self.getDy())
        x1,y1,x2,y2 = self.game.getCanvas().coords(self.getObj())
        for a in self.game.getAliens():
            if self.game.getCanvas().find_withtag(a.getObj()) != ():
                tagA = self.game.getCanvas().find_withtag(a.getObj())[0]
                if tagA in self.game.getCanvas().find_overlapping(x1,y1,x2,y2):
                    a.removeLives(1)
                    self.destroy()
                    return

        if not self.inBounds():
            self.destroy()
            return

        self.game.getRoot().after(5,lambda : self.update())   

class MissileAlien(Missile):


    def __init__(self, game, x, y, tipe):
        super().__init__(game,0,3)
        self.tipe = tipe
        col = "yellow"
        size = 9
        if self.tipe == "strong":
            col ="pink"
            size = 6
        obj = self.game.getCanvas().create_oval(x+12,y+30,x+12+size,y+30+size, fill= col)
        self.setObj(obj)
        

    def update(self):

        if self.tipe == "strong":

            if self.game.getCanvas().coords(self.game.getVaisseau().getObj()) != []:
                a1,b1,a2,b2 = self.game.getCanvas().coords(self.game.getVaisseau().getObj())
                a = a1 + 15
                x1,y1,x2,y2 = self.game.getCanvas().coords(self.getObj())
                x = x1 + 6
                l = a - x 
                if l!= 0:
                    self.setDx(l*3/abs(l))
                else:
                    self.setDx(0)

            else:
                self.destroy()
                return

        self.game.getCanvas().move(self.getObj(),self.getDx(),self.getDy())

        if self.hitbox( self.game.getVaisseau().getObj() ) == True:
            self.game.destroyVaisseau()
            self.destroy()
            return

        for b in self.game.getBlocs():

            if self.hitbox( b.getObj() ) == True:
                b.removeLives(1)
                self.destroy()
                return

        self.setDx(0)
        self.game.getRoot().after(20,lambda : self.update())


class Bloc(Entity):

    def __init__(self, game, x, y):
        super().__init__(game,2,0,0)
        obj = self.game.getCanvas().create_rectangle(x,y,x+20,y+20,fill="blue")
        self.setObj(obj)

