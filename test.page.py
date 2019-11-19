from tkinter import *
from cities import *

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


def get_circle_coordinates(line):
    """
    line input format: str,str,float(x),float(y)
    returns x1,y1,x2,y2 from x,y where xn/yn +- 5; needed to circle coordinates
    """
    x = line[2]
    y = line[3]
    x1 = y1 = (x + 2.5)
    x2 = y2 = (y - 2.5)
    return x1, y1, x2, y2

print(get_circle_coordinates(['harry', 'prior', 20, 50]))
