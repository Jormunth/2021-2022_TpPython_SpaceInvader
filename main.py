
from tkinter import Image, PhotoImage, Tk, Label, Button, Text, StringVar, Frame, Canvas, Entry
from tkinter.constants import LEFT, RIGHT, TOP
from alien import AlienStrong, AlienWeak

def m(event):
    print(event.char,a.getDx())
    if event.char == "q": 
        a.setDx(-10)
    elif event.char == "d":
        a.setDx(10)
    if event.char == "z": 
        a.setDy(-10)
    elif event.char == "s":
        a.setDy(10)

def l(event):
    if event.char == "q": 
        a.setDx(0)
    elif event.char == "d":
        a.setDx(0)
    if event.char == "z": 
        a.setDy(0)
    elif event.char == "s":
        a.setDy(0)

root=Tk()

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

a = AlienWeak(caneva)
#root.bind("<Key>", m)
#root.bind("<KeyRelease>", l)

bouton1= Button(root, text="START")
bouton1.pack(pady=10)
bouton2= Button(root, text="QUIT", command=quit)
bouton2.pack(pady=10)
def update():
    print(a.getDx(),a.getDy())
    caneva.move(a.getObj(),a.getDx(),a.getDy())
    root.after(20,update)
update()

root.mainloop()