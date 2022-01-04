
from tkinter import Event, Image, PhotoImage, Tk, Label, Button, Text, StringVar, Frame, Canvas, Entry
from tkinter.constants import LEFT, RIGHT, TOP
from alien import AlienStrong,AlienWeak
from player import Missile, Vaisseau

root=Tk()
X1=380
Y1=380
X2=420
Y2=420

def update2():
    global b
    #b = Missile(caneva,caneva.coords(a.truc)[0],caneva.coords(a.truc)[1],caneva.coords(a.truc)[2],caneva.coords(a.truc)[3])
    #b = caneva.create_rectangle(caneva.coords(a.truc)[0]+15,caneva.coords(a.truc)[1]+5,caneva.coords(a.truc)[2]-15,caneva.coords(a.truc)[3]-5, fill="red")
    #caneva.move(b.getObj(),b.getDx(),b.getDy())
    caneva.coords(b,0,10,10,20)
    caneva.after(5,update2)


def m(event):
    global b
    if event.char == "q": 
        if caneva.coords(a.truc)[0]<= 100:
            a.setDx(0)
        else:
            a.setDx(-10)
    elif event.char == "d":
        if caneva.coords(a.truc)[0]>= 700:
            a.setDx(0)
        else:
            a.setDx(10)
    if event.char == "z": 
        if caneva.coords(a.truc)[1]<= 10:
            a.setDy(0)
        else:
            a.setDy(-10)
    elif event.char == "s":
        if caneva.coords(a.truc)[1]>= 500:
            a.setDy(0)
        else:
            a.setDy(10)
    if event.char == " ":
        b = Missile(caneva,caneva.coords(a.truc)[0],caneva.coords(a.truc)[1],caneva.coords(a.truc)[2],caneva.coords(a.truc)[3])
        #b = caneva.create_rectangle(caneva.coords(a.truc)[0]+15,caneva.coords(a.truc)[1]+5,caneva.coords(a.truc)[2]-15,caneva.coords(a.truc)[3]-5, fill="red")
        update2()
        
def l(event):

    if event.char == "q": 
        a.setDx(0)
    elif event.char == "d":
        a.setDx(0)
    if event.char == "z": 
        a.setDy(0)
    elif event.char == "s":
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

a = Vaisseau(caneva,X1,Y1,X2,Y2)
b = 0
root.bind("<Key>", m)
root.bind("<KeyRelease>", l)

bouton1= Button(root, text="START")
bouton1.pack(pady=10)
bouton2= Button(root, text="QUIT", command=quit)
bouton2.pack(pady=10)


def update():
    print(a.getDx(),a.getDy())
    caneva.move(a.getObj(),a.getDx(),a.getDy())
    print(caneva.coords(a.truc))    
    caneva.after(50,update)

update()


root.mainloop()





