from entity import Entity
from tkinter import Canvas

class Alien(Entity):
    def __init__(self,root,canvas, lives,x1,y1,x2,y2):
        super().__init__(root,canvas,lives,5,0,x1,y1,x2,y2,4)
        self.compte = 1
        

    def update(self):
        self.canvas.move(self.getObj(),self.getDx(),self.getDy())
        x1,y1,x2,y2 = self.canvas.coords(self.getObj())

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

        elif x2 >= self.canvas.winfo_width() :
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

        self.root.after(40,lambda : self.update())

class AlienWeak(Alien):
    def __init__(self, root, canvas,x1,y1,x2,y2):
        super().__init__(root,canvas,3,x1,y1,x2,y2)
        obj = self.canvas.create_rectangle(self.x1,self.y1,self.x2+30,self.y2+30,fill="green")
        self.setObj(obj)
        
        
#class AlienStrong(Alien):
 #   def __init__(self, root, canvas,x1,y1,x2,y2):
 #       super().__init__(root,canvas,10,x1,y1,x2,y2)
  #      self.__object = self.canvas.create_rectangle(0, 0, 10, 10,fill="red")



