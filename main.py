
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
        b = Missile(root,caneva,x1,y1,x2,y2,l)
        b.update()
        
def keyUp(event):
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

X1=caneva.winfo_width() + 10
Y1=caneva.winfo_height() + 10
X2=caneva.winfo_width() + 10
Y2=caneva.winfo_height() + 10


a = Vaisseau(root,caneva,X1+300,Y1+400,X2+300,Y2+400)
A1 = AlienWeak(root,caneva,X1,Y1,X2,Y2)
A2 = AlienWeak(root,caneva,X1+40,Y1,X2+40,Y2)
A3 = AlienWeak(root,caneva,X1+80,Y1,X2+80,Y2)
A4 = AlienWeak(root,caneva,X1+120,Y1,X2+120,Y2)

l=[A1.getObj(),A2.getObj(),A3.getObj(),A4.getObj()]

#def creennemi():
    #nb=0
    #A1 = AlienWeak(root,caneva,X1+40*nb,Y1,X2+40*nb,Y2)
    #A1.update()
    #while nb <= A1.getnb():
     #   nb+=1
      #  A1 = AlienWeak(root,caneva,X1+40*nb,Y1,X2+40*nb,Y2)
       # A1.update()   
    
    #return A1

a.update()
A1.update()
A2.update()
A3.update()
A4.update()
#creennemi()
    

root.bind("<Key>", keyDown)
root.bind("<KeyRelease>", keyUp)

bouton1= Button(root, text="START")
bouton1.pack(pady=10)
bouton2= Button(root, text="QUIT", command=quit)
bouton2.pack(pady=10)

root.mainloop()















