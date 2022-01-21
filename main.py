
#programme principale qui permet d'afficher et lancer le jeux à l'aide des class
#game, alien, entity, player

from ctypes import resize
from tkinter import Event, Image, PhotoImage, Tk, Label, Button, Text, StringVar, Frame, Canvas, Entry
from tkinter.constants import LEFT, RIGHT, TOP
from player import MissileVaisseau
from game import Game


root=Tk()

# Fonction qui se déclenche lors de l'appuie d'une touche et qui permet de tirer et déplacer le vaisseau.
# Ainsi qu'utiliser le cheat code.
# La fonction a pour parametre "event" quie correspond a l'evenement <Key>
def keyDown(event):
    if game.getStatus() == "running":
        a = game.getVaisseau()
        if caneva.coords(a.getObj()) == []:
            return
    x1,y1,x2,y2 = caneva.coords(a.getObj())
    if event.char == "q" or event.char == "a":
        if x1 <= 0:
            a.setDx(0)
        else:
            a.setDx(-10)
    elif event.char == "d":
        if x2 >= caneva.winfo_width() :
            a.setDx(0)
        else:
            a.setDx(10)
    if event.char == " ":
        if game.getVaisseau().getCanShoot() == 0:
            b = MissileVaisseau(game,x1,y1)
            b.update()
            game.getVaisseau().setCanShoot(1)
    
    if event.char == "j":
        game.cheatCode()
    
# Fonction qui s'active au relachement d'une touche et permet de stopper le déplacement du vaisseau.
# La fonction a pour parametre "event" quie correspond a l'evenement <KeyRelease>
def keyUp(event):
    if game.getStatus() == "running":
        a = game.getVaisseau()
        if event.char == "q" or event.char == "a" and a.getDx() < 0 : 
            a.setDx(0)
        if event.char == "d" and a.getDx() > 0 : 
            a.setDx(0)

# creation de la fenetre Tkinter
root.geometry("900x600")
root.title("Space invader")
root.config(bg="BLACK")   
# instanciation du fond d'écran du canvas 
fond=PhotoImage(file='images/plane-img.gif')
frame=Frame(root, background="yellow",)
frame.pack(side='top')

# création de l'affichage de la vie et du score
text1 = StringVar()
text1.set("score: 0")
Lab1= Label(frame, textvariable=text1).pack(side='left')
text2 = StringVar()
text2.set("Lives: 3")
Lab2= Label(frame, textvariable=text2).pack(side='right')

# creation du canvas avec l'image de fond "fond"
caneva=Canvas(root, height=500, width=800)
caneva.create_image(0,0, image=fond, anchor="nw")
caneva.pack(side=LEFT)

# creation de l'objet game
game = Game(root,caneva,text1,text2)

root.bind("<Key>", keyDown)
root.bind("<KeyRelease>", keyUp)

# bouton de lancement d'une partie
bouton1= Button(root, text="START", command=lambda: game.startGame())
bouton1.pack(pady=10)
# bouton pour quitter le jeux
bouton2= Button(root, text="QUIT", command=quit)
bouton2.pack(pady=10)

root.mainloop()





