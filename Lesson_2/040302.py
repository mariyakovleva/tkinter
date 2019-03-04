from tkinter import*
root=Tk()
root.geometry('500x100')
btn1=Button(root, text='Button1')
btn1.grid(row=0,column=0, padx=2)

ent1=Entry(root, width=30)
ent1.grid(row=2, column=1,columnspan=4, sticky=S, padx=40)

btn2=Button(root, text='Button2')
btn2.grid(row=0,column=1, padx=2)          

btn3=Button(root, text='Button3')
btn3.grid(row=0,column=2, padx=2)

btn4=Button(root, text='Button4')
btn4.grid(row=0,column=3, padx=2)

root.mainloop()
