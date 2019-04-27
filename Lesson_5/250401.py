from tkinter import*
from random import randint,choice
root=Tk()
fr=Frame()
fr.pack(pady=5)

colors=['green','blue','red','blue','pink']
canv = Canvas(root,width=400,height=400)
canv.pack()
def draw_20_cirle_count_red(event):
    count=0
    for i in range(20):
        R=randint(10,40)
        x=randint(R,400-R)
        y=randint(R,400-R)
        color=choice(colors)
        canv.create_oval(x-R,y-R,x+R,y+R,fill=color)
        if color=='red':
            count+=1
    print(count,'circle(s)')
def draw_while_not_red(event):
    for i in range(20):
        R=randint(10,40)
        x=randint(R,400-R)
        y=randint(R,400-R)
        color=choice(colors)
        canv.create_oval(x-R,y-R,x+R,y+R,fill=color)
        if color=='red':
            break
def clear(event):
    canv.delete(ALL)

btn1=Button(fr,text='Draw and Count')
btn1.pack(side=LEFT)
btn1.bind('<1>',draw_20_cirle_count_red)

btn2=Button(fr,text='Draw while not red')
btn2.pack(side=LEFT,padx=10)
btn2.bind('<1>',draw_while_not_red)

btn3=Button(fr,text='Clear')
btn3.pack(side=LEFT,padx=10)
btn3.bind('<1>',clear)

root.mainloop()
