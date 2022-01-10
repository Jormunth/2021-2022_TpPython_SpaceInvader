from alien import AlienWeak, AlienStrong
from player import Bloc, Vaisseau 
import tkinter.font as tkFont

class Game():

    def __init__(self,root,canvas,txt):
        self.__aliens = []
        self.root = root
        self.canvas = canvas
        self.__score = 0
        self.vaisseau = None
        self.txtScore = txt
        self.status = "stopped"
        self.__blocs = []
        f = tkFont.Font(family='Helvetica', size=36, weight='bold')
        self.txtDisplay = self.canvas.create_text(300,200,text="Welcome",fill="white",font=f,justify="center")

    def addAlien(self,entity,x,y):
        if entity == "alienW":
            e = AlienWeak(self,x,y)
        elif entity == "alienS":
            e = AlienStrong(self,x,y)
        self.__aliens.append(e)
        e.update()

    def addBloc(self,x,y,z):
        b = Bloc(self,self.canvas.winfo_width()/z+x, self.canvas.winfo_height()-y)
        b.update()
        self.__blocs.append(b)
        print(self.__blocs)

    def getCanvas(self):
        return self.canvas

    def getRoot(self):
        return self.root

    def getVaisseau(self):
        return self.vaisseau
    
    def getBlocs(self):
        return self.__blocs

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

    def destroyBloc(self,bloc):
        self.__blocs.remove(bloc)
        bloc.destroy()

    def startGame(self):
        if self.status == "stopped":
            self.status="running"
            self.canvas.delete(self.txtDisplay)
            self.vaisseau = Vaisseau(self, self.canvas.winfo_width()/2-20, self.canvas.winfo_height()-40)
            self.vaisseau.update()
            self.update()
            self.updateSpeedAliens()
            self.setScore(0)
            self.addBloc(5,80,8)
            self.addBloc(25,80,8)
            self.addBloc(45,80,8)
            self.addBloc(5,100,8)
            self.addBloc(25,100,8)
            self.addBloc(45,100,8)
            self.addBloc(-10,80,2)
            self.addBloc(10,80,2)
            self.addBloc(30,80,2)
            self.addBloc(-10,100,2)
            self.addBloc(10,100,2)
            self.addBloc(30,100,2)
            self.addBloc(210,80,2)
            self.addBloc(230,80,2)
            self.addBloc(250,80,2)
            self.addBloc(210,100,2)
            self.addBloc(230,100,2)
            self.addBloc(250,100,2)
        else :
            print("Game is already running.")

    def getStatus(self):
            return self.status

    def gameOver(self):
        self.status="stopped"
        f = tkFont.Font(family='Helvetica', size=36, weight='bold')
        self.txtDisplay = self.canvas.create_text(300,200,text="Game Over",fill="red",font=f,justify="center")

    def spawnAliens(self):
        X=10
        Y=10
        self.addAlien("alienW", X,Y)
        self.addAlien("alienW", X+40,Y)
        self.addAlien("alienS", X+80,Y)
        self.addAlien("alienW", X+120,Y)
        self.addAlien("alienW", X+160,Y)

    def update(self):
        if self.status == "running":
            self.spawnAliens()
            self.getRoot().after(6000,lambda : self.update())