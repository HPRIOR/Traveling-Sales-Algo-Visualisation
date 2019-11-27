from tkinter import *

'''
def enter(event):
    c1.itemconfigure('c1', fill='green')
    c2.itemconfigure('c2', fill='red')


def leave(event):
    c2.itemconfigure('c2', fill='green')
    c1.itemconfigure('c1', fill='red')


# try to make one canvas change something on the other
root = Tk()

c1 = Canvas(root, bg='grey', height=500, width=500)
c2 = Canvas(root, bg='grey', height=500, width=500)

oval_1 = c1.create_oval(230, 230, 270, 270, fill='red',tag='c1')
oval_2 = c2.create_oval(230, 230, 270, 270, fill='green',tag='c2')

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

canvas = Canvas(frame, bd=0, scrollregion=(0, 0, 1000, 100), yscrollcommand=yscrollbar.set, width=200, height=500)
canvas.grid(row=0, column=0, sticky=N + S + E + W)
canvas.config(scrollregion=canvas.bbox(ALL))
canvas.create_line(20, 0, 20, 200)

yscrollbar.config(command=canvas.yview)

frame.pack()

root.mainloop()
