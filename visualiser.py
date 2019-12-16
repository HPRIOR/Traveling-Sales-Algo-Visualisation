from tkinter import *
from cities import *


def oval_button_gen(canvas, target_canvas, ln, coord_list, func, tag_1, tag_2, index_1, index_2):
    """
    Ovals used as 'buttons' to reveal information
    Binding events to canvas objects requires a variable to identify
        canvas object, hence 'i = canvas...' in loop
    For each oval object, 'Leave' and 'Enter' events are created which correspond to map data
    A list of tags associated with hidden texts on map, index selects the right text from list
        corresponding to a point; len used to control first and last anomalies due to circular
        indexing
    func: HO function used to place oval buttons on different canvases with diff coordinates
    Can only bind one event to a canvas object, otherwise they overwrite each other

    """
    ind = 0
    for i in range(ln):
        # creates ovals
        i = canvas.create_oval(func(coord_list[ind], index_1, index_2), fill='green', activefill='red')

        # binds events to ovals
        canvas.tag_bind(i, '<Enter>', lambda_func(target_canvas, f=show,
                                                  tag_list_1=tag_1, tag_list_2=tag_2, index=ind, ln=ln))
        canvas.tag_bind(i, '<Leave>', lambda_func(target_canvas, f=hide,
                                                  tag_list_1=tag_1, tag_list_2=tag_2, index=ind, ln=ln))
        ind = (ind + 1) % ln


def lambda_func(canvas, f, tag_list_1, tag_list_2, index, ln):
    """
    this was needed because the ordinary lambda functions in circle_button_gen would
    not update their indices, which are required to match generate tag identifiers
    HO function allow for the use of both 'leave' and 'enter' function
    """
    return lambda e: f(e, canvas, tag_list_1[index], tag_list_2[index], ln)


def raise_lower_tag(tag, ln):
    """
    gives the tags above and below input tag
    """
    tag_minus, tag_plus = int(tag[1:]) - 1, int(tag[1:]) + 1

    if tag == tag[0] + '0':
        tag_below = tag[0] + str(ln - 1)
        tag_above = tag[0] + str(tag_plus)
        return tag_below, tag_above
    elif tag == tag[0] + str(ln - 1):
        tag_below = tag[0] + str(tag_minus)
        tag_above = tag[0] + '0'
        return tag_below, tag_above
    else:
        tag_below, tag_above = tag[0] + str(tag_minus), tag[0] + str(tag_plus)
        return tag_below, tag_above


def hide(event, canvas, tag_1, tag_2, ln):
    """
    Hides object on canvas with given tag
    """
    canvas.itemconfigure(tag_2, state=HIDDEN)
    canvas.itemconfigure(raise_lower_tag(tag_2, ln)[1], state=HIDDEN)

    canvas.itemconfigure(tag_1, state=HIDDEN)
    canvas.itemconfigure(raise_lower_tag(tag_1, ln)[0], state=HIDDEN)
    canvas.itemconfigure(raise_lower_tag(tag_1, ln)[1], state=HIDDEN)


def show(event, canvas, tag_1, tag_2, ln):
    """
    Shows object on canvas with given tag
    """
    canvas.itemconfigure(tag_2, state=NORMAL)
    canvas.itemconfigure(raise_lower_tag(tag_2, ln)[1], state=NORMAL)

    canvas.itemconfigure(tag_1, state=NORMAL)
    canvas.itemconfigure(raise_lower_tag(tag_1, ln)[0], state=NORMAL)
    canvas.itemconfigure(raise_lower_tag(tag_1, ln)[1], state=NORMAL)


def linear_coord_list(init, size, ln, mid_point):
    x = init
    lst = []
    for i in range(ln):
        tup = (mid_point, x)
        x += size
        lst.append(tup)
    return lst


def tag_gen(ln, s):
    """
    Generates tags every item on list, prefixed with string (s)
    e.g s1, s2, s3...sN
    """
    tag_list = []
    for i in range(ln):
        var = s + str(i)
        tag_list.append(var)
    return tag_list


def text_gen(canvas, x, y, text, tag, state, anchor):
    """
    Generate text at coordinates -  with tag identifier
    """
    canvas.create_text(x, y, text=text, anchor=anchor, fill='black', tag=tag, state=state)


def get_mid_coord(x1, y1, x2, y2):
    x_mid = (x1 + x2) / 2
    y_mid = (y1 + y2) / 2
    return x_mid, y_mid


def line_gen(canvas, x1, y1, x2, y2):
    """
    Generates lines between two coordinates
    """
    canvas.create_line(x1, y1, x2, y2, arrow=LAST, fill='red')


def start(canvas, road_map):
    """
    Creates the start identifier on canvas
    """
    canvas.create_line(road_map[0][2], road_map[0][3], road_map[0][2], 20, fill='red')
    canvas.create_text(road_map[0][2], 10, text='Start', fill='red')


def get_circle_coordinates(line, x, y):
    """
    line input format: str,str,float(x),float(y)
    returns x1,y1,x2,y2 from x,y where xn/yn +- circ_size; needed to circle coordinates
    """
    circ_size = 4
    x, y = line[x], line[y]
    x1, y1, x2, y2 = (x + circ_size), (y + circ_size), (x - circ_size), (y - circ_size)
    return x1, y1, x2, y2


def func_index_list(f, i, lst):
    """
    Applies a function to all the indexes within a nested loop (e.g. all the 1st items in a matrix)
    Used to find the minimum and maximum values of coordinates in a nested list (used in change_v_data below)
    """
    new_list = []
    [new_list.append(float(line[i])) for line in lst]
    func = f(new_list)
    return func


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


def distances_list(road_map):
    """
    returns a list of distances between point with last item [-1] being the distance between the first and last point
    """
    distance_list = []
    ln = len(road_map)
    ind = 0
    for i in range(ln):
        dist_string_short = '%.2f' % compute_individual_distance(road_map[ind - 1][2],
                                                                 road_map[ind - 1][3],
                                                                 road_map[ind][2],
                                                                 road_map[ind][3])
        distance_list.append(dist_string_short)
        ind = (ind + 1) % ln
    return distance_list
