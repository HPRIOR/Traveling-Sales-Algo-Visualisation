from tkinter import *

root = Tk()

frame = Frame(root, bd=2, relief=SUNKEN)

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)



yscrollbar = Scrollbar(frame)
yscrollbar.grid(row=0, column=1, sticky=N+S)


canvas = Canvas(frame, bd=0, scrollregion=(0, 0, 1000, 2000), yscrollcommand=yscrollbar.set, width= 200, height=1000)
canvas.grid(row=0, column=0, sticky=N+S+E+W)
canvas.config(scrollregion=canvas.bbox(ALL))
canvas.create_line(20, 0, 20, 200)

yscrollbar.config(command=canvas.yview)

frame.pack()

root.mainloop()