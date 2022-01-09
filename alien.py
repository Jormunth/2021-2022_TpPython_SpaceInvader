from entity import Entity
from tkinter import Canvas

class Alien(Entity):
    def __init__(self,game, lives):
        super().__init__(game,lives,5,0,4)
        self.compte = 1

    def update(self):
        canvas=self.game.getCanvas()
        canvas.move(self.getObj(),self.getDx(),self.getDy())
        x1,y1,x2,y2 = canvas.coords(self.getObj())

        #if self.hitbox(self.EV) == True:
            #self.destroy()
            #return 

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

        self.game.getRoot().after(40,lambda : self.update())

class AlienWeak(Alien):
    def __init__(self, game,x,y):
        super().__init__(game,3)
        obj = self.game.getCanvas().create_rectangle(x,y,x+30,y+30,fill="#1f1")
        self.setObj(obj)
        
class AlienStrong(Alien):
   def __init__(self, game,x,y):
        super().__init__(game,10)
        obj = self.game.getCanvas().create_rectangle(x,y,x+30,y+30,fill="green")
        self.setObj(obj)



