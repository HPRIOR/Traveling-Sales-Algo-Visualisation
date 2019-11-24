from tkinter import *


def visualise(road_map):
    window = Tk()
    window.title('Traveling salesperson app')
    window.geometry('+200+20')
    window.resizable(FALSE, FALSE)

    canvas_frame = Frame(window, width=1500, height=700, bg='gray89')
    divide_canvas = Frame(window, width=1500, height=2, bg='black')
    bottom_frame = Frame(window, width=1500, height=200)
    input_frame = Frame(bottom_frame, width=749, height=200, bg='gray89')
    divide_inpinf = Frame(bottom_frame, width=2, height=200, bg='black')
    info_frame = Frame(bottom_frame, width=749, height=200, bg='gray89')

    canvas_frame.grid(row=0, column=0)
    divide_canvas.grid(row=1, column=0)
    bottom_frame.grid(row=2, column=0)
    input_frame.grid(row=0, column=0)
    divide_inpinf.grid(row=0, column=1)
    info_frame.grid(row=0, column=2)

    window.mainloop()


visualise(1)
