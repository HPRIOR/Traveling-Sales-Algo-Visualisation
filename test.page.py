from tkinter import *
from cities import *
import random

root = Tk()
root.title('test')
root.geometry("500x500")

c = Canvas(root, width=500, height=500, bg='linen')

# oval = c.create_oval(250,250, 240 ,240, activefill='red')

# c.tag_bind(oval, '<Button-1>', draw_line)

c.create_line(250, 0, 250, 500)
c.create_line(0, 250, 500, 250)
c.create_line(0, 300, 500, 300)
c.create_line(300, 0 , 300, 500)

def hide_text(event, canvas, tag):
    canvas.itemconfigure(tag, state=HIDDEN)


def text_map_icon(event, canvas, origin_x, origin_y, text):
    canvas.create_text(origin_x, origin_y - 60, text=text, tag='icon')


def map_icon(canvas, x):
    for i in range(x):
        i = canvas.create_oval(random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), fill='green', activefill='red')
        print(i)
        canvas.tag_bind(i, '<Enter>', lambda e: text_map_icon(e, c, 250, 250, 'hello'))
        canvas.tag_bind(i, '<Leave>', lambda e: hide_text(e, c, 'icon'))

        # works just about






map_icon(c, 10)




c.pack()

root.mainloop()
