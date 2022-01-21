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
        if self.game.getStatus() == "stopped":
            self.destroy()

        canvas=self.game.getCanvas()
        if canvas.coords(self.getObj()) == []:
            return

        canvas.move(self.getObj(),self.getDx(),self.getDy())
        x1,y1,x2,y2 = canvas.coords(self.getObj())

        if self.comptetire == 0:
            self.rand = randint(40,100)

        if self.comptetire == self.rand:
            b=MissileAlien(self.game,x1,y1,self.tipe)
            b.update()
            self.comptetire = 0

        if x1 <= 0 or x2 >= canvas.winfo_width() :
            self.setDx(-1 * self.getDx())
            self.game.getCanvas().move(self.getObj(),0,self.getHeight()+5)
        elif y2 > 500 :
            self.destroy()
        self.comptetire += 1
        self.game.getRoot().after(40,lambda : self.update())

class AlienWeak(Alien):
    
    def __init__(self,game,x,y):
        super().__init__(game,2,"weak")
        obj = self.game.getCanvas().create_rectangle(x,y,x+30,y+30,fill="#1f1")
        self.setObj(obj)

    def destroy(self):
        self.game.removeAlien(self)
        print("obj destroyed")
        self.game.getCanvas().delete(self.getObj())
        self.game.increaseScore(10)
        self.game.resetCompte()
        del self
    
class AlienStrong(Alien):

   def __init__(self,game,x,y):
        super().__init__(game,4,"strong")
        obj = self.game.getCanvas().create_rectangle(x,y,x+30,y+30,fill="green")
        self.setObj(obj)

   def destroy(self):
        self.game.removeAlien(self)
        print("obj destroyed")
        self.game.getCanvas().delete(self.getObj())
        self.game.increaseScore(20)
        self.game.resetCompte()
        del self
    
