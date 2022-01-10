from alien import AlienWeak, AlienStrong
from player import Vaisseau

class Game():

    def __init__(self,root,canvas,txt):
        self.__aliens = []
        self.root = root
        self.canvas = canvas
        self.__score = 0
        self.vaisseau = None
        self.txtScore = txt
        self.status = "stopped"

    def addAlien(self,entity,x,y):
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
    
    def increaseScore(self,x):
        if self.status == "running":
            self.__score += x
            self.txtScore.set("score:" + str(self.__score))

    def setScore(self,score):
        self.__score = score
        self.txtScore.set("score:" + str(self.__score))

    def updateSpeedAliens(self):
        for a in self.__aliens:
            a.setDx( (a.getDx()/abs(a.getDx())) * 10 / len(self.__aliens) )

    def removeAlien(self,a):
        self.__aliens.remove(a)
        print(self.__aliens)
        self.updateSpeedAliens()
    
    def destroyVaisseau(self):
        self.vaisseau.destroy()

    def startGame(self):
        if self.status == "stopped":
            self.status="running"
            self.vaisseau = Vaisseau(self, self.canvas.winfo_width()/2-20, self.canvas.winfo_height()-41)
            self.vaisseau.update()
            X=10
            Y=10
            self.addAlien("alienW", X,Y)
            self.addAlien("alienW", X+40,Y)
            self.addAlien("alienW", X+80,Y)
            self.addAlien("alienS", X+120,Y)
            self.addAlien("alienS", X+160,Y)
            self.updateSpeedAliens()
            self.setScore(0)
        else :
            print("Game is already running.")

    def getStatus(self):
        return self.status

    def gameOver(self):
        self.setScore(0)
        self.status="stopped"