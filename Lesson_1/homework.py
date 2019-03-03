from tkinter import*
root=Tk()
root.geometry('350x250')

fr1=Frame(root)
fr2=Frame(root)
fr3=Frame(root)

fr1.pack(side=TOP,fill=BOTH)
fr2.pack(side=BOTTOM,fill=BOTH)
fr3.pack(anchor=CENTER)

btn1=Button(fr1,text='1',width=5,height=2)
btn1.pack(side=LEFT)

btn3=Button(fr1,text='3',width=5,height=2)
btn3.pack(side=RIGHT)

btn5=Button(fr2,text='5',width=5,height=2)
btn5.pack(side=RIGHT)

btn4=Button(fr2,text='4',width=5,height=2)
btn4.pack(side=RIGHT,padx=10)

btn2=Button(fr3,text='2',width=5,height=2)
btn2.pack(side=RIGHT)

root.mainloop()
