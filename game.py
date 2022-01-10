from alien import AlienWeak, AlienStrong
from player import Vaisseau

class Game():

    def __init__(self,root,canvas,txt):
        self.__aliens = []
        self.root = root
        self.canvas = canvas
        self.__score = 0
        self.vaisseau = None
        self.txt = txt

    def addEntity(self,entity,x,y):
        if entity == "alienW":
            e = AlienWeak(self,x,y)
        elif entity == "alienS":
            e = AlienStrong(self,x,y)
        self.__aliens.append(e)
        e.update()

    def getCanvas(self):
        return self.canvas

    def getRoot(self):
        return self.root

    def getVaisseau(self):
        return self.vaisseau

    def getAliens(self):
        return self.__aliens
    
    def setscore(self,score):
        self.__score += score
        self.txt.set("score:" + str(self.__score))

    def removeAlien(self,a):
        self.__aliens.remove(a)

    def destroyAlien(self,a):
        self.__aliens.remove(a)
        a.destroy()
    
    def destroyVaisseau(self):
        self.vaisseau.destroy()

    def startGame(self):
        self.vaisseau = Vaisseau(self, self.canvas.winfo_width()/2-20, self.canvas.winfo_height()-41)
        self.vaisseau.update()
        X=10
        Y=10
        self.addEntity("alienW", X,Y)
        self.addEntity("alienW", X+40,Y)
        self.addEntity("alienW", X+80,Y)
        self.addEntity("alienS", X+120,Y)
        self.addEntity("alienS", X+160,Y)

