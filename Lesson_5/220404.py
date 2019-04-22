from tkinter import *
from random import randint, choice
root = Tk()
colors=['green', 'blue', 'red', 'blue', 'pink']
canv = Canvas(root,width=400,height=400)
canv.pack()

for i in range(12):
    R = randint(10, 40)
    x = randint(R, 400 - R)
    y = randint(R, 400 - R)
    color=choice(colors)
    canv.create_oval(x-R, y-R, x+R, y+R, fill=color)

root.mainloop()
