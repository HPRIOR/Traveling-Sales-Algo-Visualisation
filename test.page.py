from tkinter import *
from cities import *
import random

def draw_line(event):
    x1, y1, x2, y2 = random.randint(0, 490), random.randint(0, 390), random.randint(0, 490), random.randint(0, 390)
    c.create_line(x1, y1, x2, y2)


root = Tk()
root.title('test')
root.geometry("500x500")

frame_1 = Frame(root, width=500, height=100,  bg='white')
border = Frame(root, width=500, height=1, bg='black')
frame_2 = Frame(root, width=500, height=399, bg='white')
frame_2.pack_propagate(False)
frame_1.pack_propagate(False)

c = Canvas(frame_2, width=490, height=390, bg='linen')

oval = c.create_oval(250,250, 200 ,200, activefill='red')

c.tag_bind(oval, '<Button-1>', draw_line)




c.pack_propagate(False)

frame_2.pack()
border.pack()
frame_1.pack()

c.pack()

root.mainloop()

