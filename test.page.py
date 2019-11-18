from tkinter import *
from cities import *

'''def change_visualise_data(road_map):
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
    main_win.mainloop()'''

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

'''road_map = read_cities('test-city-data-2.txt')
x_min, x_max, y_min, y_max = find_min_max_x_y(road_map)
print(x_min)
visualise(road_map)
'''

'''lst = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


def find_minmax_list_index(f, i, lst):
    """
    applies a function to all the indexes within a nested loop (e.g. all the 1st items in a matrix)
    """
    new_list = []
    [new_list.append(float(line[i])) for line in lst]
    min_max = f(new_list)
    return min_max


road_map = read_cities('city-data.txt')
print(find_minmax_list_index(min, 2, lst))
'''


root = Tk()
root.title('This is an example window')
root.geometry('500x500')
frame1 = Frame(root, width=250, height=250, bg='black')
frame1.grid(row=0, column=0)

frame2 = Frame(root, width=250, height=250, bg='red')
frame2.grid(row=0, column=1)
#frame1.grid_propagate(False)
frame2.grid_propagate(False)

label = Label(frame2, text="this is a test", bg='red').grid(column=2)

root.mainloop()


