from tkinter import *
from cities import *


def change_visualise_data(road_map):
    data_road_map = []
    [data_road_map.append(list(line)) for line in road_map]
    for line in data_road_map:
        line[2] = (float(line[2]) + 90)
        line[3] = (float(line[3]) + 180)
    return data_road_map


def find_min_max_x_y(road_map):
    x, y = [], []
    for line in road_map:
        x.append(line[2])
        y.append(line[3])
    x_min = float(min(x))
    x_max = float(max(x))
    y_min = float(min(y))
    y_max = float(max(y))
    return x_min, x_max, y_min, y_max

def visualise(road_map):
    road_map = change_visualise_data(road_map)
    main_win = Tk()
    main_win.geometry('360x180')
    canv = Canvas(main_win, background='white', height=360, width=180)
    canv.pack(fill=BOTH, anchor='center')
    ln = len(road_map)
    ind = 0
    for i in range(ln):
        canv.create_line(road_map[ind - 1][2], road_map[ind - 1][3],
                         road_map[ind][2], road_map[ind][3])
        ind = (ind + 1) % ln
    main_win.mainloop()


'''
def checkered(canvas, line_distance):
    # vertical lines at an interval of "line_distance" pixel
    for x in range(line_distance, canvas_width, line_distance):
        canvas.create_line(x, 0, x, canvas_height, fill="#476042")
    # horizontal lines at an interval of "line_distance" pixel
    for y in range(line_distance, canvas_height, line_distance):
        canvas.create_line(0, y, canvas_width, y, fill="#476042")


master = Tk()
canvas_width = 200
canvas_height = 100
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

checkered(w, 10)

mainloop()
'''


road_map = read_cities('test-city-data-2.txt')
x_min, x_max, y_min, y_max = find_min_max_x_y(road_map)
print(x_min)
#visualise(road_map)
