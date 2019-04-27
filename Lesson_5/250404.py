from tkinter import*
from random import randint,choice
root=Tk()
fr=Frame()
fr.pack(pady=5)

colors=['green','blue','red','blue','pink']
canv = Canvas(root,width=400,height=400)
canv.pack()
def draw_20_cirle_green_and_blue(event):
    count_green=0
    count_blue=0
    for i in range(20):
        R=randint(10,40)
        x=randint(R,400-R)
        y=randint(R,400-R)
        color=choice(colors)
        canv.create_oval(x-R,y-R,x+R,y+R,fill=color)
        if color=='green':
            count_green+=1
        if color=='blue':
           count_blue+=1
        if count_green==3 and count_green==3:
            break
def clear(event):
    canv.delete(ALL)

btn1=Button(fr,text='Draw')
btn1.pack(side=LEFT)
btn1.bind('<1>',draw_20_cirle_green_and_blue)

btn2=Button(fr,text='Clear')
btn2.pack(side=LEFT,padx=10)
btn2.bind('<1>',clear)

root.mainloop()


