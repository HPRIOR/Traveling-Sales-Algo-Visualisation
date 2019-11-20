from tkinter import *
from cities import *
import random

'''root = Tk()
root.title('This is an example window')
root.geometry('500x500')
c = Canvas(root, width=500, height=500)


c.create_line(0,500,500,0)
c.create_oval(25,25,35,35)

c.addtag_all('hello')
c.pack()
root.mainloop()

'''

def draw_line():
    x1, y1, x2, y2 = random.randint(0, 390), random.randint(0, 390), random.randint(0, 390), random.randint(0,390)
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
b = Button_1(Frame_1)


frame_2.pack()
border.pack()
frame_1.pack()

c.pack()

root.mainloop()
