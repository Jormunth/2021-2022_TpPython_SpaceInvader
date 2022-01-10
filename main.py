
from tkinter import Event, Image, PhotoImage, Tk, Label, Button, Text, StringVar, Frame, Canvas, Entry
from tkinter.constants import LEFT, RIGHT, TOP
from alien import AlienWeak, AlienStrong
from player import Missile, Vaisseau, MissileVaisseau, MissileAlien
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
    if event.char == " ":
        b = MissileVaisseau(game,x1+a.getWidth()/2,y1,[])
        b.update()
    
    
def keyUp(event):
    a = game.getVaisseau()
    if event.char == "q" or event.char == "a" and a.getDx() < 0 : 
        a.setDx(0)
    if event.char == "d" and a.getDx() > 0 : 
        a.setDx(0)

root.geometry("900x600")
root.title("Space invader")
root.config(bg="BLACK")    
fond=PhotoImage(file='space.gif')

frame=Frame(root, background="yellow",)
frame.pack(side='top')

text1 = StringVar()
text1.set("score: 0")
Lab1= Label(frame, textvariable=text1).pack(side='left')

Lab2= Label(frame,text="lives").pack(side='right')

caneva=Canvas(root, height=500, width=800)
caneva.create_image(0, 0, image=fond)
caneva.pack(side=LEFT)

game = Game(root,caneva,text1)

root.bind("<Key>", keyDown)
root.bind("<KeyRelease>", keyUp)

bouton1= Button(root, text="START", command=lambda: game.startGame())
bouton1.pack(pady=10)
bouton2= Button(root, text="QUIT", command=quit)
bouton2.pack(pady=10)

root.mainloop()



