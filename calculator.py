import math
from tkinter import*
root=Tk()
root.geometry("210x245")

def number_button(num):
    ent1.insert(END, str(num))

def clear():
    ent1.delete(0,END)

def clear2():
    n=text1.get()
    ent1.delete(len(n)-1)

def sqrt():
    s = int(text1.get())
    f=math.sqrt(s)
    clear()
    ent1.insert(0, f)

def factorial():
    s = int(text1.get())
    f=1
    for i in range(1,s+1):
        f*=i
    clear()
    ent1.insert(0, f)

def iquel():
    s=ent1.get()
    try:
        result = eval(s)
        clear()
        ent1.insert(0, result)
    except Exception:
        clear()
        ent1.insert(0, "Error!")


root.resizable(0,0)

root.title("Калькулятор")

ent1 =Entry(root,width=28,justify='right') 
ent1.grid(row=1,column=0,columnspan=15,padx=5,pady=5,ipadx=14,ipady=15)

btn1=Button(root,text="MC",font="Times 10",width=4,height=1,)
btn1.grid(row=3,column=0,padx=2,pady=2)
btn2=Button(root,text="MR",font="Times 10",width=4,height=1)
btn2.grid(row=3,column=1,padx=2,pady=2)
btn3=Button(root,text="MS",font="Times 10",width=4,height=1)
btn3.grid(row=3,column=2,padx=2,pady=2)
btn4=Button(root,text="M+",font="Times 10",width=4,height=1)
btn4.grid(row=3,column=3,padx=2,pady=2)
btn5=Button(root,text="M-",font="Times 10",width=4,height=1)
btn5.grid(row=3,column=4,padx=2,pady=2)

btn6=Button(root,text="n!",font="Times 10",width=4,height=1)
btn6.grid(row=4,column=0,padx=2,pady=2)
btn7=Button(root,text="CE",font="Times 10",width=4,height=1,command=clear)
btn7.grid(row=4,column=1,padx=2,pady=2)
btn8=Button(root,text="C",font="Times 10",width=4,height=1,command=clear2)
btn8.grid(row=4,column=2,padx=2,pady=2)
btn9=Button(root,text="sqrt",font="Times 10",width=4,height=1)
btn9.grid(row=4,column=3,padx=2,pady=2)
btn10=Button(root,text="^",font="Times 10",width=4,height=1)
btn10.grid(row=4,column=4,padx=2,pady=2)

btn11=Button(root,text="7",font="Times 10",width=4,height=1, command=lambda:number_button(7))
btn11.grid(row=5,column=0,padx=2,pady=2)
btn12=Button(root,text="8",font="Times 10",width=4,height=1, command=lambda:number_button(8))
btn12.grid(row=5,column=1,padx=2,pady=2)
btn13=Button(root,text="9",font="Times 10",width=4,height=1, command=lambda:number_button(9))
btn13.grid(row=5,column=2,padx=2,pady=2)
btn14=Button(root,text="/",font="Times 10",width=4,height=1,command=lambda:number_button('/'))
btn14.grid(row=5,column=3,padx=2,pady=2)
btn15=Button(root,text="(",font="Times 10",width=4,height=1,command=lambda:number_button('('))
btn15.grid(row=5,column=4,padx=2,pady=2)

btn16=Button(root,text="4",font="Times 10",width=4,height=1,command=lambda:number_button(4))
btn16.grid(row=6,column=0,padx=2,pady=2)
btn17=Button(root,text="5",font="Times 10",width=4,height=1,command=lambda:number_button(5))
btn17.grid(row=6,column=1,padx=2,pady=2)
btn18=Button(root,text="6",font="Times 10",width=4,height=1,command=lambda:number_button(6))
btn18.grid(row=6,column=2,padx=2,pady=2)
btn19=Button(root,text="*",font="Times 10",width=4,height=1,command=lambda:number_button('*'))
btn19.grid(row=6,column=3,padx=2,pady=2)
btn20=Button(root,text=")",font="Times 10",width=4,height=1,command=lambda:number_button(')'))
btn20.grid(row=6,column=4,padx=2,pady=2)

btn21=Button(root,text="1",font="Times 10",width=4,height=1,command=lambda:number_button(1))
btn21.grid(row=7,column=0,padx=2,pady=2)
btn22=Button(root,text="2",font="Times 10",width=4,height=1,command=lambda:number_button(2))
btn22.grid(row=7,column=1,padx=2,pady=2)
btn23=Button(root,text="3",font="Times 10",width=4,height=1,command=lambda:number_button(3))
btn23.grid(row=7,column=2,padx=2,pady=2)
btn24=Button(root,text="-",font="Times 10",width=4,height=1,command=lambda:number_button('-'))
btn24.grid(row=7,column=3,padx=2,pady=2)
btn25=Button(root,text="=",font="Times 10",width=4,height=3,command=iquel)
btn25.grid(row=7,column=4,rowspan=2)

btn26=Button(root,text="0",font="Times 10",width=10,height=1,command=lambda:number_button(0))
btn26.grid(row=8,column=0,columnspan=2,padx=2,pady=2)
btn27=Button(root,text=",",font="Times 10",width =4,height=1,command=lambda:number_button(','))
btn27.grid(row=8,column=2,padx=2,pady=2)
btn28=Button(root,text="+",font="Times 10",width=4,height=1,command=lambda:number_button('+'))
btn28.grid(row=8,column=3,padx=2,pady=2)


root.mainloop()


