from tkinter import *
from cities import *

road_map = read_cities('city-data.txt')


def change_visualise_data(road_map, canvas_max_size_x, canvas_max_size_y, c_edge):
    """
    canvas_max_size_x,y: max size for canvas in x,y directions
    c_edge: border size around edge of canvas
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


def visualise(road_map):
    canvas_size_x = 1500
    canvas_size_y = 700

    # the total distance prior to data normalisation
    prior_compute = compute_total_distance(road_map)

    # normalise data
    road_map = change_visualise_data(road_map, canvas_size_x, canvas_size_y, 2)

    # create main tk window
    window = Tk()
    window.title('Traveling salesperson app')
    window.geometry('+200+20')
    window.resizable(FALSE, FALSE)

    # create frames
    canvas_frame = Frame(window, width=canvas_size_x, height=canvas_size_y, bg='gray89')
    divide_canvas = Frame(window, width=1500, height=2, bg='black')
    bottom_frame = Frame(window, width=1500, height=200)
    input_frame = Frame(bottom_frame, width=749, height=200, bg='gray89')
    divide_inpinf = Frame(bottom_frame, width=2, height=200, bg='black')
    info_frame = Frame(bottom_frame, width=749, height=200, bg='gray89')

    # organise frames
    canvas_frame.grid(row=0, column=0)
    divide_canvas.grid(row=1, column=0)
    bottom_frame.grid(row=2, column=0)
    input_frame.grid(row=0, column=0)
    divide_inpinf.grid(row=0, column=1)
    info_frame.grid(row=0, column=2)

    # canvas for coordinates
    canv = Canvas(canvas_frame, width=canvas_size_x, height=canvas_size_y)
    canv.grid(row=0, column=0)


    window.mainloop()


visualise(road_map)
