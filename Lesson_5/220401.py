from tkinter import *
root = Tk()

canv = Canvas(root,width=800,height=550, bg='white')
canv.pack()
canv.create_oval(30,30,90,90, fill='red')


root.mainloop()
