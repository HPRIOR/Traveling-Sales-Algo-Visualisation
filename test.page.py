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



def text_map_icon(event, canvas, origin_x, origin_y, text):
    canvas.create_text(origin_x, origin_y - 60, text=text)


def map_icon(canvas, origin_x, origin_y, text):
    icon = canvas.create_arc((origin_x - 50), (origin_y + 50), (origin_y + 50), (origin_x - 50), start=70, extent=40,
                             fill='green', activefill='red', activewidth=2.0)

    # canvas.tag_bind(icon, '<Enter>', lambda e: text_map_icon(e, c, origin_x, origin_y, text))




map_icon(c, 250, 250, 'map icon')

map_icon(c, 300, 300, 'map icon')

# c.create_arc(200, 200, 300, 300)

c.pack()

root.mainloop()
