from tkinter import *
from random import randint, choice
root = Tk()
canv = Canvas(root,width=400,height=400)
canv.pack()
for i in range(10):
    R = randint(10, 40)
    x = randint(R, 400 - R)
    y = randint(R, 400 - R)
    canv.create_oval(x-R, y-R, x+R, y+R, fill='pink')
root.mainloop()
