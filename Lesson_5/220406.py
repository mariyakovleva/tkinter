from tkinter import *
from random import randint, choice
root = Tk()
fr = Frame()
fr.pack(pady = 5)
colors=['green', 'blue', 'red', 'blue', 'pink']
canv = Canvas(root,width=400,height=400)
canv.pack()
def draw_20_cirle_count_red_or_green(event):
    count_red=0
    count_green=0
    for i in range(20):
        R=randint(10,40)
        x=randint(R,400-R)
        y=randint(R,400-R)
        color=choice(colors)
        canv.create_oval(x-R,y-R,x+R,y+R,fill=color)
        if color=='red':
            count_red+=1
        if color=='green':
           count_green+=1
    print(count_red,'red circle(s)',count_green,'green circle(s)')
            
def draw_while_not_red_or_green(event):
    for i in range(20):
        R=randint(10,40)
        x=randint(R,400-R)
        y=randint(R,400-R)
        color=choice(colors)
        canv.create_oval(x-R,y-R,x+R,y+R,fill=color)
        if color=='red'or color=='green':
            break
def clear(event):
    canv.delete(ALL)

btn1=Button(fr,text='Draw and Count')
btn1.pack(side=LEFT)
btn1.bind('<1>',draw_20_cirle_count_red_or_green)

btn2=Button(fr,text ='Draw while not red or green')
btn2.pack(side =LEFT, padx=10)
btn2.bind('<1>',draw_while_not_red_or_green)

btn3=Button(fr,text='Clear')
btn3.pack(side=LEFT,padx=10)
btn3.bind('<1>',clear)

root.mainloop()

