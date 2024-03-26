from tkinter import *
from random import randrange

root=Tk()
root.geometry("400x400")
root.title("MOn canvas")
root.config(background="orange")
root.minsize(400,400)

COLORS=["tomato", "blue", "green", "purple"]
R=20

cnv=Canvas(root, scrollregion =(0, 0, 800, 800),
width=350, height=350, bg="ivory")
cnv.pack()

cnv["xscrollincrement"]=100
14
for _ in range(500):
    A=[randrange(800) for _ in range(2)]
    B=A[0]+R, A[1]+R
    cnv.create_rectangle(A, B, fill=COLORS[randrange(4)])

def xscroll():
    cnv.xview_scroll(1, "units")
    cnv.after(1500, xscroll)

xscroll()

root.mainloop()