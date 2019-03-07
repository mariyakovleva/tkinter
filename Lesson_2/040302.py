from tkinter import*
root=Tk()
root.geometry('500x100')
btn1=Button(root, text='Button1')
btn1.grid(row=0,column=0, padx=2)

ent1=Entry(root, width=37)
ent1.grid(row=2, column=0,columnspan=10, sticky=E)

btn2=Button(root, text='Button2')
btn2.grid(row=0,column=1, padx=2)          

btn3=Button(root, text='Button3')
btn3.grid(row=0,column=2, padx=2)

btn4=Button(root, text='Button4')
btn4.grid(row=0,column=3, padx=2)

btn5=Button(root, text='Button5')
btn5.grid(row=1,column=0, padx=2,pady=2)

btn6=Button(root, text='Button6')
btn6.grid(row=1,column=1, padx=2,pady=2)

btn7=Button(root, text='Button7')
btn7.grid(row=1,column=2, padx=2,pady=2)

btn8=Button(root, text='Button8')
btn8.grid(row=1,column=3, padx=2,pady=2)

root.mainloop()
