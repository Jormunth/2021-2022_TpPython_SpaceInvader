from tkinter import Image, PhotoImage, Tk, Label, Button, Text, StringVar, Frame, Canvas, Entry
from tkinter.constants import LEFT, RIGHT, TOP, X
from entity import Entity

#class enfant de entity contenant les class vaisseaux
class Vaisseau(Entity):

    def __init__(self, game, x, y):
        
        super().__init__(game,3,0,0)
        obj = self.game.getCanvas().create_rectangle(x,y,x+40,y+40,fill="orange")
        self.setObj(obj)
        self.__canShoot = 0

    def setCanShoot(self,s):
        self.__canShoot = s

    def getCanShoot(self):
        return self.__canShoot

    # update modifie la trajectoire d'un canvas objets de classe vaiseau en le déplacant selon x ou Y puis en 
    # réitérant la fonction au bout de 20 ms
    def update(self):
        canvas = self.game.getCanvas()
        canvas.move(self.getObj(),self.getDx(),self.getDy())
        if canvas.coords(self.getObj()) == []:
            return
        x1,y1,x2,y2 = canvas.coords(self.getObj())
        if x1 < 0 :
            canvas.coords(self.getObj(),0,y1,40,y2)
        elif x2 > canvas.winfo_width() :
            canvas.coords(self.getObj(),760,y1,800,y2)
        if y1 < 0 :
            canvas.coords(self.getObj(),x1,0,x2,40)
        if y2 > canvas.winfo_height() :
            canvas.coords(self.getObj(),x1,460,x2,500)

        if self.__canShoot > 0 :
            if self.__canShoot > 4:
                self.__canShoot = 0
            else:
                self.__canShoot +=1
        self.game.getRoot().after(20,lambda : self.update())
        
    def getLives(self):
        return self.lives

    def removeLives(self, x):
        self.lives -= x
        self.game.updateLives()
        print(self.lives)
        if self.lives == 0:
            self.destroy()

    def destroy(self):
        print("obj destroyed")
        self.game.gameOver()
        self.game.getCanvas().delete(self.getObj())
        del self

#les class MissileVaisseaux et MissileAlien permettent de gerer la trajectoire des missiles des 
#entites respectives
class Missile(Entity):

    def __init__(self,game,x,y):
        super().__init__(game,1,x,y)

class MissileVaisseau(Missile):
    #creation du missile sous forme rectangulaire
    def __init__(self, game, x, y):
        super().__init__(game,0,-10)
        obj = self.game.getCanvas().create_rectangle(x+23,y+17,x-3+20,y-17,fill="red")
        self.setObj(obj)
    # fonction qui permet de deplacer le missile vers le haut 
    # si le missile touche un Alien il le détruit et se détruit
    # la fonction est relancer au bout de 5 ms 
    def update(self):
        if self.game.getStatus() == "gameOver":
            self.destroy()
        # permet de voir si le missile est sur l'Alien
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
        #relance la fonction
        self.game.getRoot().after(5,lambda : self.update())   

class MissileAlien(Missile):
    #creation du missile alien rond dont la taille et la couleur varie en fonction de Alien strong et Alien weak
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
        
    #fonction qui permet de deplacer le missile vers le bas ou de suivre le vaisseaux(si alien strong tire) 
    #si le missile touche un bloc ou le vaisseaux il le détruit et se détruit
    #la fonction est relancer au bout de 20 ms
    def update(self):
        if self.game.getStatus() == "stopped":
            self.destroy()

        if self.tipe == "strong":

            #si Alien strong le missile va dans la direction du vaisseaux
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
        
        #repere si le missile est sur le vaisseau et le détruit
        if self.hitbox( self.game.getVaisseau().getObj() ) == True:
            self.game.getVaisseau().removeLives(1)
            self.destroy()
            return
        #repere si le missile est sur un bloc et le détruit
        for b in self.game.getBlocs():
            if self.hitbox( b.getObj() ) == True:
                b.removeLives(1)
                self.destroy()
                return

        self.setDx(0)
        self.game.getRoot().after(20,lambda : self.update())


class Bloc(Entity):
    # class qui creer des blocs  permmettant de proteger le vaisseaux
    def __init__(self, game, x, y):
        super().__init__(game,2,0,0)
        obj = self.game.getCanvas().create_rectangle(x,y,x+20,y+20,fill="blue")
        self.setObj(obj)

    def update(self):
        return super().update()

