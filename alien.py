from entity import Entity
from tkinter import Canvas
from random import randint
from player import MissileAlien, MissileVaisseau



class Alien(Entity):
    
    def __init__(self,game, lives, tipe):
        super().__init__(game,lives,5,0)
        self.compte = 1
        self.comptetire = 0
        self.rand = 1
        self.tipe = tipe

    def update(self):
        canvas=self.game.getCanvas()
        if canvas.coords(self.getObj()) == []:
            return

        canvas.move(self.getObj(),self.getDx(),self.getDy())
        x1,y1,x2,y2 = canvas.coords(self.getObj())

        if self.comptetire == 0:
            self.rand = randint(10,90)

        if self.comptetire == self.rand:
            b=MissileAlien(self.game,x1,y1,self.tipe)
            b.update()
            self.comptetire = 0

        if x1 <= 0 :
            self.setDx(0)

            if y1 < 30*self.compte:
                self.setDy(2)
                return self.update()

            else:
                self.setDy(0)
                self.compte+=1
                self.setDx(5)

        elif x2 >= canvas.winfo_width() :
            self.setDx(0)

            if y1 < 30*self.compte:
                
                self.setDy(2)
                return self.update()

            else:
                self.setDy(0)
                self.compte+=1
            self.setDx(-5)

        elif y2 > 500 :
            self.destroy()
        self.comptetire += 1
        self.game.getRoot().after(40,lambda : self.update())

    def destroy(self):
        self.game.removeAlien(self)
        super().destroy()

class AlienWeak(Alien):
    
    def __init__(self,game,x,y):
        super().__init__(game,3,"weak")
        obj = self.game.getCanvas().create_rectangle(x,y,x+30,y+30,fill="#1f1")
        self.setObj(obj)

    def destroy(self):

        print("obj destroyed")
        self.game.getCanvas().delete(self.getObj())
        self.game.setscore(10)
        del self
    
class AlienStrong(Alien):

   def __init__(self,game,x,y):
        super().__init__(game,5,"strong")
        obj = self.game.getCanvas().create_rectangle(x,y,x+30,y+30,fill="green")
        self.setObj(obj)

   def destroy(self):
        print("obj destroyed")
        self.game.getCanvas().delete(self.getObj())
        self.game.setscore(20)
        del self
    