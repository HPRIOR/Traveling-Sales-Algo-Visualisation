from tkinter import *
from itertools import count
'''

def enter(event):
    c1.itemconfigure('c1', fill='green')
    c2.itemconfigure('c2', fill='red')


def leave(event):
    c2.itemconfigure('c2', fill='green')
    c1.itemconfigure('c1', fill='red')

def print_x(event):
    c1.create_text(200, 200, text='hello')

# try to make one canvas change something on the other
root = Tk()

c1 = Canvas(root, bg='grey', height=500, width=500)
c2 = Canvas(root, bg='grey', height=500, width=500)

oval_1 = c1.create_oval(230, 230, 270, 270, fill='red',tag='c1')
oval_2 = c2.create_oval(230, 230, 270, 270, fill='green', tag='c2')

c1.tag_bind(oval_1, '<Enter>', enter)
c1.tag_bind(oval_1, '<Leave>', leave)

c2.tag_bind(oval_2, '<Enter>', enter)
c2.tag_bind(oval_2, '<Leave>', leave)



c1.pack()
c2.pack()

mainloop()'''


root = Tk()
frame = Frame(root, bd=2, relief=SUNKEN)

#frame.grid_rowconfigure(0, weight=1)
#frame.grid_columnconfigure(0, weight=1)

yscrollbar = Scrollbar(frame)
yscrollbar.grid(row=0, column=1, sticky=N + S)

canvas = Canvas(frame, bd=0, scrollregion=(0, 0, 0, 10000), yscrollcommand=yscrollbar.set, width=200, height=500)
canvas.grid(row=0, column=0, sticky=N + S + E + W)
canvas.config(scrollregion=canvas.bbox(ALL))

yscrollbar.config(command=canvas.yview)

x1, y1, x2, y2 = 100, 20, 100, 130
text_coord = 60
canvas.create_text(100, 10, text='start')

for i in range(20):
    canvas.create_line(x1, y1, x2, y2, arrow=LAST)
    canvas.create_text(150, text_coord, text='distance')
    y1 += 150
    y2 += 150
    text_coord += 150




frame.pack()

root.mainloop()

def linear_coord_list(init, size, ln):
    x = init
    lst = []
    for i in range(ln):
        lst.append(x)
        x += size
    return lst



