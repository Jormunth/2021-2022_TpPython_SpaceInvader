
from tkinter import Image, PhotoImage, Tk, Label, Button, Text, StringVar, Frame, Canvas, Entry
from tkinter.constants import LEFT, RIGHT, TOP

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

bouton1= Button(root, text="START")
bouton1.pack(pady=10)
bouton2= Button(root, text="QUIT", command=quit)
bouton2.pack(pady=10)
root.mainloop()
