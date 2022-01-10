from alien import AlienWeak, AlienStrong
from player import Bloc, Vaisseau 

class Game():

    def __init__(self,root,canvas,txt):
        self.__aliens = []
        self.root = root
        self.canvas = canvas
        self.__score = 0
        self.vaisseau = None
        self.__blocs = []
        self.txt = txt

    def addEntity(self,entity,x,y):
        if entity == "alienW":
            e = AlienWeak(self,x,y)
        elif entity == "alienS":
            e = AlienStrong(self,x,y)
        self.__aliens.append(e)
        e.update()

    def addBloc(self,x,y,z):
        b = Bloc(self,self.canvas.winfo_width()/z+x, self.canvas.winfo_height()-y)
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

    def destroyBloc(self,bloc):
        self.__blocs.remove(bloc)
        bloc.destroy()

    def startGame(self):
        self.vaisseau = Vaisseau(self, self.canvas.winfo_width()/2-20, self.canvas.winfo_height()-40)
        self.vaisseau.update()
        X=10
        Y=10
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
        self.addEntity("alienW", X+40,Y)
        self.addEntity("alienW", X+80,Y)
        self.addEntity("alienS", X+120,Y)
        self.addEntity("alienS", X+160,Y)


