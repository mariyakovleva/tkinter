from tkinter import*
root=Tk()
root.geometry("210x245")

root.title("Калькулятор")
ent1 =Entry(root,width=28) 
ent1.grid(row=1,column=0,columnspan=15,padx=5,pady=5,ipadx=14,ipady=15)

btn1=Button(root,text="MC",font="Times 10",width=4,height=1)
btn1.grid(row=3,column=0,padx=2,pady=2)
btn2=Button(root,text="MR",font="Times 10",width=4,height=1)
btn2.grid(row=3,column=1,padx=2,pady=2)
btn3=Button(root,text="MS",font="Times 10",width=4,height=1)
btn3.grid(row=3,column=2,padx=2,pady=2)
btn4=Button(root,text="M+",font="Times 10",width=4,height=1)
btn4.grid(row=3,column=3,padx=2,pady=2)
btn5=Button(root,text="M-",font="Times 10",width=4,height=1)
btn5.grid(row=3,column=4,padx=2,pady=2)

btn6=Button(root,text="←",font="Times 10",width=4,height=1)
btn6.grid(row=4,column=0,padx=2,pady=2)
btn7=Button(root,text="CE",font="Times 10",width=4,height=1)
btn7.grid(row=4,column=1,padx=2,pady=2)
btn8=Button(root,text="C",font="Times 10",width=4,height=1)
btn8.grid(row=4,column=2,padx=2,pady=2)
btn9=Button(root,text="+/-",font="Times 10",width=4,height=1)
btn9.grid(row=4,column=3,padx=2,pady=2)
btn10=Button(root,text="sqrt",font="Times 10",width=4,height=1)
btn10.grid(row=4,column=4,padx=2,pady=2)

btn11=Button(root,text="7",font="Times 10",width=4,height=1)
btn11.grid(row=5,column=0,padx=2,pady=2)
btn12=Button(root,text="8",font="Times 10",width=4,height=1)
btn12.grid(row=5,column=1,padx=2,pady=2)
btn13=Button(root,text="9",font="Times 10",width=4,height=1)
btn13.grid(row=5,column=2,padx=2,pady=2)
btn14=Button(root,text="/",font="Times 10",width=4,height=1)
btn14.grid(row=5,column=3,padx=2,pady=2)
btn15=Button(root,text="%",font="Times 10",width=4,height=1)
btn15.grid(row=5,column=4,padx=2,pady=2)

btn16=Button(root,text="4",font="Times 10",width=4,height=1)
btn16.grid(row=6,column=0,padx=2,pady=2)
btn17=Button(root,text="5",font="Times 10",width=4,height=1)
btn17.grid(row=6,column=1,padx=2,pady=2)
btn18=Button(root,text="6",font="Times 10",width=4,height=1)
btn18.grid(row=6,column=2,padx=2,pady=2)
btn19=Button(root,text="*",font="Times 10",width=4,height=1)
btn19.grid(row=6,column=3,padx=2,pady=2)
btn20=Button(root,text="1/x",font="Times 10",width=4,height=1)
btn20.grid(row=6,column=4,padx=2,pady=2)

btn21=Button(root,text="1",font="Times 10",width=4,height=1)
btn21.grid(row=7,column=0,padx=2,pady=2)
btn22=Button(root,text="2",font="Times 10",width=4,height=1)
btn22.grid(row=7,column=1,padx=2,pady=2)
btn23=Button(root,text="3",font="Times 10",width=4,height=1)
btn23.grid(row=7,column=2,padx=2,pady=2)
btn24=Button(root,text="-",font="Times 10",width=4,height=1)
btn24.grid(row=7,column=3,padx=2,pady=2)
btn25=Button(root,text="=",font="Times 10",width=4,height=3)
btn25.grid(row=7,column=4,rowspan=2)

btn26=Button(root,text="0",font="Times 10",width=10,height=1)
btn26.grid(row=8,column=0,columnspan=2,padx=2,pady=2)
btn27=Button(root,text=",",font="Times 10",width =4,height=1)
btn27.grid(row=8,column=2,padx=2,pady=2)
btn28=Button(root,text="+",font="Times 10",width=4,height=1)
btn28.grid(row=8,column=3,padx=2,pady=2)

root.mainloop()
