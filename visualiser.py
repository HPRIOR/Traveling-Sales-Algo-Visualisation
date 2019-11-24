import cities

def change_visualise_data(road_map, canvas_max_size_x, canvas_max_size_y, c_edge):
    """
    canvas_max_size_x,y: max size for canvas in x,y directions
    c_edge: border size around edge of canvas

    returns normalised data for visualisation function

    removes minus values, shifts all to corner, then spreads them out, makes corrects x,y for long,lat

    return: state, city, x(float), y(float)
    """

    data_road_map = []
    [data_road_map.append(list(line)) for line in road_map]

    # removes minus values
    for line in data_road_map:
        line[2] = (float(line[2]) + 90)  # x
        line[3] = (float(line[3]) + 180)  # y
        # long-lat
        line[3], line[2] = line[2], line[3]

    x_min, y_min = func_index_list(min, 2, data_road_map), \
                   func_index_list(min, 3, data_road_map)

    # shift all coordinates to one corner of canvas
    for line in data_road_map:
        line[2] = (line[2] - (x_min - c_edge))  # x
        line[3] = (line[3] - (y_min - c_edge))  # y

    x_max, y_max = func_index_list(max, 2, data_road_map), \
                   func_index_list(max, 3, data_road_map)

    factor_x, factor_y = canvas_max_size_x / (x_max + c_edge), canvas_max_size_y / (y_max + c_edge)

    # spreads data out through canvas
    for line in data_road_map:
        line[2] = line[2] * factor_x  # x
        line[3] = line[3] * factor_y  # y
        # flips along x axis due to tkinter's (0,0) being on the top-left
        line[3] = canvas_max_size_y - line[3]
    return data_road_map


def get_circle_coordinates(line):
    """
    line input format: str,str,float(x),float(y)
    returns x1,y1,x2,y2 from x,y where xn/yn +- 5; needed to circle coordinates
    """
    circ_size = 2.5
    x = line[2]
    y = line[3]
    x1, y1, x2, y2 = (x + circ_size), (y + circ_size), (x - circ_size), (y - circ_size)
    return x1, y1, x2, y2


def func_index_list(f, i, lst):
    """
    applies a function to all the indexes within a nested loop (e.g. all the 1st items in a matrix)
    used to find the minimu m and maximum values of coordinates in a nested list
    """
    new_list = []
    [new_list.append(float(line[i])) for line in lst]
    func = f(new_list)
    return func


def map_icon(canvas, origin_x, origin_y):
    icon = canvas.create_arc((origin_x - 50), (origin_x - 50), (origin_y + 50), (origin_y + 50), start=70, extent=40,
                             fill='green', activefill='red', activewidth=2.0)


def visualise(road_map):
    canvas_size_x = 1500
    canvas_size_y = 700
    prior_compute = compute_total_distance(road_map)
    road_map = change_visualise_data(road_map, canvas_size_x, canvas_size_y, 2)

    main_win = Tk()
    main_win.geometry("%dx%d" % (canvas_size_x + 100, canvas_size_y + 100))

    lab = Label(main_win, text='the total distance is: %f' % prior_compute)
    lab.pack()

    canv = Canvas(main_win, height=canvas_size_y, width=canvas_size_x)
    canv.pack()
    canv.create_line(0, (canvas_size_y / 2), canvas_size_x, canvas_size_y / 2)
    canv.create_line(canvas_size_x / 2, 0, canvas_size_x / 2, canvas_size_y)

    # visualising road_map
    ln = len(road_map)
    ind = 0
    for i in range(ln):
        # dots for cities
        canv.create_oval(get_circle_coordinates(road_map[ind]))
        # map_icons
        map_icon(canv, road_map[ind][2], road_map[ind][3])
        # text
        canv.create_text(road_map[ind - 1][2], road_map[ind - 1][3], text=road_map[ind - 1][0], anchor=N, fill='red')
        # lines between cities
        canv.create_line(road_map[ind - 1][2], road_map[ind - 1][3], road_map[ind][2], road_map[ind][3], arrow=LAST,
                         fill='blue')
        ind = (ind + 1) % ln
    print(road_map)
    main_win.mainloop()
