from tkinter import *
from cities import *
import random

def draw_line():
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

photo = PhotoImage(file="icon.png")

c = Canvas(frame_2, width=490, height=390, bg='linen')
b = Button(c, text='button', command=draw_line, image=photo)
label = Label(c, image=photo)
label.bind('<Button-1>', lambda e: draw_line)
label.pack
c.pack_propagate(False)
c.create_window(250, 250, window=b)

frame_2.pack()
border.pack()
frame_1.pack()

c.pack()

root.mainloop()

