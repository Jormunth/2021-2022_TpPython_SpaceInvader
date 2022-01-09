
from tkinter import Event, Image, PhotoImage, Tk, Label, Button, Text, StringVar, Frame, Canvas, Entry
from tkinter.constants import LEFT, RIGHT, TOP
from alien import AlienWeak, AlienStrong
from player import Missile, Vaisseau
from game import Game

root=Tk()

def keyDown(event):
    a = game.getVaisseau()
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
    if event.char == "z" or event.char == "w":
        if y1 <= 0:
            a.setDy(0)
        else:
            a.setDy(-10)
    elif event.char == "s":
        if y2 >= caneva.winfo_height() :
            a.setDy(0)
        else:
            a.setDy(10)
        
    if event.char == " ":
        b = Missile(game,x1,y1,[])
        b.update()
        
def keyUp(event):
    a = game.getVaisseau()
    if event.char == "q" or event.char == "a" and a.getDx() < 0 : 
        a.setDx(0)
    if event.char == "d" and a.getDx() > 0 : 
        a.setDx(0)
    if event.char == "z" or event.char == "w" and a.getDy() < 0 : 
        a.setDy(0)
    if event.char == "s" and a.getDy() > 0 : 
        a.setDy(0)
    

root.geometry("900x600")
root.title("Space invader")
root.config(bg="BLACK")    
fond=PhotoImage(file='space.gif')

frame=Frame(root, background="yellow",)
frame.pack(side='top')

Lab1= Label(frame, text="score:").pack(side='left')
Lab2= Label(frame,text="lives").pack(side='right')

caneva=Canvas(root, height=500, width=800)
caneva.create_image(0, 0, image=fond)
caneva.pack(side=LEFT)

X=10
Y=10

game = Game(root,caneva)
game.addEntity("alienW", X,Y)
game.addEntity("alienW", X+40,Y)
game.addEntity("alienW", X+80,Y)
game.addEntity("alienS", X+120,Y)

root.bind("<Key>", keyDown)
root.bind("<KeyRelease>", keyUp)

bouton1= Button(root, text="START")
bouton1.pack(pady=10)
bouton2= Button(root, text="QUIT", command=quit)
bouton2.pack(pady=10)

root.mainloop()
