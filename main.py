
from tkinter import Event, Image, PhotoImage, Tk, Label, Button, Text, StringVar, Frame, Canvas, Entry
from tkinter.constants import LEFT, RIGHT, TOP
from alien import AlienWeak
from player import Missile, Vaisseau

root=Tk()

def keyDown(event):
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
        b = Missile(root,caneva,x1,y1,l)
        b.update()
    
def keyUp(event):
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

Lab1= Label(frame, text="score:").pack(side='left')
Lab2= Label(frame,text="lives").pack(side='right')

caneva=Canvas(root, height=500, width=800)
caneva.create_image(0, 0, image=fond)
caneva.pack(side=LEFT)

X1= 10
Y1= 10

a = Vaisseau(root,caneva,X1+300,Y1+400)
A1 = AlienWeak(root,caneva,X1,Y1)
A2 = AlienWeak(root,caneva,X1+40,Y1)
A3 = AlienWeak(root,caneva,X1+80,Y1)
A4 = AlienWeak(root,caneva,X1+120,Y1)

l=[A1.getObj(),A2.getObj(),A3.getObj(),A4.getObj()]

a.update()
A1.update()
A2.update()
A3.update()
A4.update()

root.bind("<Key>", keyDown)
root.bind("<KeyRelease>", keyUp)

bouton1= Button(root, text="START")
bouton1.pack(pady=10)
bouton2= Button(root, text="QUIT", command=quit)
bouton2.pack(pady=10)

root.mainloop()





