from tkinter import*
from random import randint,choice
root=Tk()
fr=Frame()
fr.pack(pady=5)

colors=['green','blue','red','blue','pink']
canv = Canvas(root,width=400,height=400)
canv.pack()
def draw_20_cirle_count_red_and_blue(event):
    count_min=0
    count_max=0
    for i in range(20):
        R=randint(10,80)
        x=randint(R,400-R)
        y=randint(R,400-R)
        color=choice(colors)
        canv.create_oval(x-R,y-R,x+R,y+R,fill=color)
        if R<20 and color=='red':
            count_min+=1
        if R>50 and color=='blue':
           count_max+=1
    print(count_min,'red circle(s)',count_max,'blue circle(s)')
            
def draw_while_not_red_and_blue(event):
    for i in range(20):
        R=randint(10,40)
        x=randint(R,400-R)
        y=randint(R,400-R)
        color=choice(colors)
        canv.create_oval(x-R,y-R,x+R,y+R,fill=color)
        if color=='red'or color=='blue':
            break
def clear(event):
    canv.delete(ALL)

btn1=Button(fr,text='Draw and Count')
btn1.pack(side=LEFT)
btn1.bind('<1>',draw_20_cirle_count_red_and_blue)

btn2=Button(fr,text ='Draw while not red and blue')
btn2.pack(side =LEFT, padx=10)
btn2.bind('<1>',draw_while_not_red_and_blue)

btn3=Button(fr,text='Clear')
btn3.pack(side=LEFT,padx=10)
btn3.bind('<1>',clear)

root.mainloop()

