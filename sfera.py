from tkinter import *
from tkinter import ttk

def sfera(*args)
    r=msg_Entry.get()
    r=int(r)
    volume=(4.0/3.0) * 3.14 * r**3
    print(volume)
    msg_label.set(volume)


root=Tk()
root.title(" ")

mainframe=ttk.Frame(root,padding="20 30 20 30")
mainframe.grid(column=0, row=0)

msg_Label=StringVar()
msg_Entry=StringVar()
rag=ttk.Label(mainframe, text="inserisci il raggio").grid(column=0,row=0)
R=ttk.Entry(mainframe, width=3, textvariable=msg_Entry).grid(column=1,row=0)
Button=ttk.Button(mainframe,text="calcolo= ",command=Sfera).grid(column=1,row=1)
vol=ttk.Label(mainframe, text="volume= ").grid(column=0,row=2)
v=ttk.Label(mainframe,textvariable=msg_Label).grid(column=1, row=2)

root.mainloop()
