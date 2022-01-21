from tkinter.constants import X

# Cette classe permet de gérer les entités tel que les vaisseaux, les missiles et les blocs
# chaque objet est définie par un nombre de vie, des vitesse de déplacement dx et dy 
# et d'un objet qui permettra l'affichage sur le canvas.
# Cette classe permet de leguer des fonctions et attributs pres definit pour toutes les entites.
class Entity():
    
    def __init__(self,game,lives,dx,dy):
        self.lives = lives
        self.game = game
        self.__object = None
        self.__dx = dx
        self.__dy = dy

    def setlives(self,vie):
        self.lives = vie
        
    def setObj(self,obj):
        self.__object = obj

    def getObj(self):
        if self.__object == None:
            return False
        else:
            return self.__object

    def getDx(self):
        return self.__dx

    def getDy(self):
        return self.__dy

    def setDx(self,x):
        self.__dx = x

    def setDy(self,y):
        self.__dy = y

    def getWidth(self):
        x1,y1,x2,y2 = self.game.getCanvas().coords(self.getObj())
        return x2 - x1

    def getHeight(self):
        x1,y1,x2,y2 = self.game.getCanvas().coords(self.getObj())
        return y2 - y1

    def update(self):
        #fonction qui permet de bouger l'entité et qui repeter au bout d'un certains temps
        if self.game.getStatus() == "stopped":
            self.destroy()
        self.game.getCanvas().move(self.getObj(),self.getDx(),self.getDy())
        self.game.getRoot().after(20,lambda : self.update())

    def inBounds(self):
        #fonction qui check si un objet entity est à l'exterieur du canvas
        #retourne False si c'est le cas sinon True
        if self.game.getCanvas().coords(self.getObj()) == []:
            return True
        x1,y1,x2,y2 = self.game.getCanvas().coords(self.getObj())
        if x2 < 0 or x1 > self.game.getCanvas().winfo_width() :
            print("out of bounds X")
            return False
        if y2 < 0 or y1 > self.game.getCanvas().winfo_height() :
            print("out of bounds Y")
            return False
        return True

    def destroy(self):
        #fonction qui détruit un objet sur le canvas
        self.game.getCanvas().delete(self.getObj())
        del self
    
    def removeLives(self, x):
        #fonction qui retire une vies à l'entité et la détruit si sa vie est à 0
        self.lives -= x
        print(self.lives)
        if self.lives == 0:
            self.destroy()

    def hitbox(self,x):
        #cette fonction prend un autre objet en entrée et regarde si cet objet est sur l'objet entité 
        #il retourne True si c'est le cas
        if self.game.getCanvas().coords(self.getObj()) == []:
            return False
        else:
            x1,y1,x2,y2 = self.game.getCanvas().coords(self.getObj())
       
        if self.game.getCanvas().coords(x) == []:
            return False
        else:
            a1,b1,a2,b2 = self.game.getCanvas().coords(x)
        
        if x1 < a2 and x2 > a1 and y1 < b2 and y2 > b1:
            return True
            
        

