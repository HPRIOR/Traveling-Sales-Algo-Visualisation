from tkinter import *
from cities import *
import random

'''def draw_line():
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
b = Button(frame_1, text='button', command=draw_line)


b.pack()
frame_2.pack()
border.pack()
frame_1.pack()

c.pack()

root.mainloop()
'''

list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sorted(list_1[1]))
