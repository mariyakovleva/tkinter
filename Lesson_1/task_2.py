from tkinter import*
root=Tk()
root.geometry('350x250')

fr1=Frame(root)
fr2=Frame(root)

fr1.pack(side=TOP,fill=BOTH)
fr2.pack(side=BOTTOM,fill=BOTH)

btn1=Button(fr1,text='Ok_1')
btn1.pack(side=LEFT)

btn2=Button(fr1,text='Ok_2')
btn2.pack(side=RIGHT)

btn3=Button(fr2,text='Ok_3')
btn3.pack(side=LEFT)

btn4=Button(fr2,text='Ok_4')
btn4.pack(side=RIGHT)

root.mainloop()
