class Entity():
    def __init__(self,canvas,lives,dx,dy):
        self.__lives = lives
        self.canvas = canvas
        self.__object = None
        self.__dx = dx
        self.__dy = dy
        
    def setObj(self,obj):
        self.__object = obj

    def getObj(self):
        return self.__object

    def getDx(self):
        return self.__dx

    def getDy(self):
        return self.__dy

    def setDx(self,x):
        self.__dx = x

    def setDy(self,y):
        self.__dy = y