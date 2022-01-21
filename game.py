from alien import AlienWeak, AlienStrong
from player import Bloc, Vaisseau 
import tkinter.font as tkFont
from tkinter import PhotoImage
from random import randint

# Cette classe permet de gerer une partie de space inavader.
# Attributs:
#     - root : <tkinter.Tk> fenetre principale
#     - canvas : <tkinter.Canvas>
#     - aliens : List(<Alien>)
#     - score : <int>
#     - vaisseau : <Vaisseau>
#     - txtScore : <StringVar>
#     - txtLives : <StringVar>
#     - status : <str>
#     - blocs : List(<Bloc>)
#     - compte : <int> nombre d'aliens
#     - txtDisplay : <tkinter.Canvas.Text> texte d'information = (Game Over, Welcome)
class Game():
    # initialise la partie
    def __init__(self,root,canvas,txtScore,txtLives):
        self.__aliens = []
        self.root = root
        self.canvas = canvas
        self.__score = 0
        self.vaisseau = None
        self.txtScore = txtScore
        self.txtLives = txtLives
        self.status = "stopped"
        self.__blocs = []
        self.compte = 0
        f = tkFont.Font(family='Helvetica', size=36, weight='bold')
        self.txtDisplay = self.canvas.create_text(400,250,text="Welcome",fill="white",font=f,justify="center")

    # detruit tous les vaisseux aliens (pas les missiles)
    def cheatCode(self):
        print(self.__aliens)
        if self.status == "running":
            while self.__aliens:
                self.__aliens[0].destroy()
        print(self.__aliens)

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
    
    def getCompte(self):
        return self.compte

    def resetCompte(self):
        self.compte = self.compte-1

    def getAliens(self):
        return self.__aliens
    
    # augmente le score par x
    def increaseScore(self,x):
        if self.status == "running":
            self.__score += x
            self.txtScore.set("score:" + str(self.__score))

    # met a jour le nombre de vie sur le canvas
    def updateLives(self):
        self.txtLives.set("Lives:" + str(self.vaisseau.getLives()))

    # change le score et l'affiche
    def setScore(self,score):
        self.__score = score
        self.txtScore.set("score:" + str(self.__score))

    # change la vitesse des aliens en fonctions du nombre total d'aliens (encore des bugs)
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

    # Commence la partie, spawn le vaisseau, plusieurs aliens, et des blocs de protection.
    def startGame(self):
        if self.status == "stopped":
            self.status="running"
            self.canvas.delete(self.txtDisplay)
            self.vaisseau = Vaisseau(self, self.canvas.winfo_width()/2-20, self.canvas.winfo_height()-40)
            self.vaisseau.update()
            self.spawnAliens()
            self.update()
            self.updateSpeedAliens()
            self.setScore(0)
            self.updateLives()
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

    # Fini la partie, le joueur peut recommencer en cliquant sur start.
    # set le status a "stopped", sur le prochain update les objets se detruiront par eux memes
    def gameOver(self):
        self.status="stopped"
        f = tkFont.Font(family='Helvetica', size=36, weight='bold')
        self.txtDisplay = self.canvas.create_text(400,250,text="Game Over",fill="red",font=f,justify="center")

    # Spawn les premiers Aliens
    def spawnAliens(self):
        X=10
        Y=10
        self.addAlien("alienW", X,Y)
        self.compte+=1
        self.addAlien("alienW", X+40,Y)
        self.compte+=1
        self.addAlien("alienS", X+80,Y)
        self.compte+=1
        self.addAlien("alienW", X+120,Y)
        self.compte+=1
        self.addAlien("alienW", X+160,Y)
        self.compte+=1

    #  Spawn un Alien
    def spawn2(self):
        X=10
        Y=10
        x = randint(0,10)
        if x>=3:
            self.addAlien("alienW", X,Y)
            self.compte+=1
        else:
            self.addAlien("alienS", X,Y)
            self.compte+=1
        
    # Fait apparaitre un alien toute les "rep" millisecondes.
    def update(self):
        if self.status == "running":
            rep= 1000*self.compte
            if self.compte<=10:
                self.spawn2()
            self.getRoot().after(rep,lambda : self.update())
