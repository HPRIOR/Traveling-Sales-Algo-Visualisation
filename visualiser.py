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
    """
    :param init: starting point on canvas
    :param size: distance between coords
    :param ln: length of road map
    :param mid_point: the distance between
    :return: list of coordinates for use in linear part of visualiser
    """
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


def start(canvas, road_map, total_distance):
    """
    Creates the start identifier on canvas
    With total distance too
    """
    start_text = 'Start (distance: %.2f)' % total_distance
    canvas.create_line(road_map[0][2], road_map[0][3], road_map[0][2], 20, fill='red')
    canvas.create_text(road_map[0][2], 10, text=start_text, fill='red')


def get_circle_coordinates(tple, x, y):
    """
    tuple input format: str,str,float(x),float(y)
    returns x1,y1,x2,y2 from x,y where xn/yn +- circ_size; needed to circle coordinates
    """
    circ_size = 4
    x, y = tple[x], tple[y]
    x1, y1, x2, y2 = (x + circ_size), (y + circ_size), (x - circ_size), (y - circ_size)
    return x1, y1, x2, y2


def func_index_list(f, index, lst):
    """
    Applies list method to all the indexes within a nested list
    (e.g. all the 1st items in a matrix). Used to find the minimum and maximum
    values of coordinates in a nested list (used in change_v_data below)
    """
    new_list = []
    [new_list.append(float(line[index])) for line in lst]
    return f(new_list)


def normalise_data(road_map, canvas_max_size_x, canvas_max_size_y, c_edge):
    """
    canvas_max_size_x,y: max size for canvas in x,y directions
    c_edge: border size around edge of canvas
    return: state, city, x(float), y(float)
    """

    data_road_map = []
    [data_road_map.append(list(line)) for line in road_map]

    min_x = func_index_list(min, 2, data_road_map)
    min_y = func_index_list(min, 3, data_road_map)

    for line in data_road_map:
        line[2] = (float(line[2]) + abs(min_y))  # x
        line[3] = (float(line[3]) + abs(min_x))  # y
        # long-lat
        line[3], line[2] = line[2], line[3]

    new_x_min, new_y_min = func_index_list(min, 2, data_road_map), \
                           func_index_list(min, 3, data_road_map)

    # shift all coordinates to one corner of canvas
    for line in data_road_map:
        line[2] = (line[2] - (new_x_min - c_edge))  # x
        line[3] = (line[3] - (new_y_min - c_edge))  # y

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
    returns a list of distances between point with last item [-1] being the
    distance between the first and last point
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


def visualise(road_map):
    ln = len(road_map)  # length needed for functions below
    total_distance = compute_total_distance(road_map)

    # geometry variables defined so that changes will effect whole window
    canvas_height, canvas_width = 825, 1350
    scroll_width = 200
    divider_width = 2
    window_width = canvas_width + scroll_width + divider_width
    size_scroll_coord = 100

    # get numbers list to use for linear coords
    linear_coord = linear_coord_list(40, size_scroll_coord, ln, int(scroll_width / 2.5))
    scroll_distance = linear_coord[-1][1] + 30

    # get info prior to normalisation
    distances = distances_list(road_map)

    # normalise data
    road_map = normalise_data(road_map, canvas_width, canvas_height, c_edge=2)

    # create main tk window
    window = Tk()
    window.title('Traveling salesperson app')
    window.geometry('+100+0')
    window.resizable(FALSE, FALSE)

    # pop-up window
    top_window = Toplevel()
    top_window.title("Important information")
    top_window.attributes('-topmost', 'true')
    top_window.geometry('+500+300')
    msg = Message(top_window, text='!! Attention traveling salesperson !! \n '
                                   '\n'
                                   'Hover over the green dots with cursor to view information about the distances '
                                   'between incoming and '
                                   'outgoing cities. \n '
                                   '\n'
                                   'The green dots on the linear map to the right also reveal information on the main '
                                   'map (this can be scrolled up and down).')
    msg.pack()
    top_window_button = Button(top_window, text='OK', command=top_window.destroy)
    top_window_button.pack()

    # create frames
    top_frame = Frame(window, width=window_width, height=canvas_height)
    canvas_frame = Frame(top_frame, width=canvas_width, height=canvas_height, bg='gray89')
    scroll_frame = Frame(top_frame)
    scroll_frame_divider = Frame(top_frame, width=divider_width, height=canvas_height, bg='black')
    scrollbar = Scrollbar(scroll_frame)

    # organise frames
    canvas_frame.grid(row=0, column=0)
    scroll_frame_divider.grid(row=0, column=3)
    scroll_frame.grid(row=0, column=4)
    scrollbar.grid(row=0, column=1, sticky=N + S)
    top_frame.grid(row=0, column=0)

    # canvas' for coordinates
    canv = Canvas(canvas_frame, width=canvas_width, height=canvas_height)
    canv_scroll = Canvas(scroll_frame, width=scroll_width, height=canvas_height,
                         yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, scroll_distance))
    canv_scroll.config(scrollregion=canv_scroll.bbox(ALL))
    scrollbar.config(command=canv_scroll.yview)

    # organise canvases
    canv_scroll.grid(row=0, column=0)
    canv.grid(row=0, column=0)

    # create tags to identify text
    city_tag = tag_gen(ln, 'A')
    distance_tag = tag_gen(ln, 'D')

    # create start and finish indicators
    start(canv, road_map, total_distance)

    # generate stuff on canvas
    canv_scroll.create_text(scroll_width / 2.5, 10, text='Start')
    canv_scroll.create_text(scroll_width / 2.5, linear_coord[-1][1] + 20, text='End')
    ind = 0

    for i in range(ln):
        dist_coord_x, dist_coord_y = get_mid_coord(road_map[ind - 2][2], road_map[ind - 2][3], road_map[ind - 1][2],
                                                   road_map[ind - 1][3])

        # generate lines
        line_gen(canv, road_map[ind - 1][2], road_map[ind - 1][3], road_map[ind][2], road_map[ind][3])
        if ind < ln - 1:
            line_gen(canv_scroll, linear_coord[ind][0], linear_coord[ind][1] + 10,
                     linear_coord[ind][0], linear_coord[ind][1] + (size_scroll_coord - 10))

        # generate city text
        text_gen(canv, road_map[ind - 1][2], (road_map[ind - 1][3] - 5), text=road_map[ind - 1][1],
                 tag=city_tag[ind - 1], state=HIDDEN, anchor=S)
        text_gen(canv_scroll, scroll_width / 2, linear_coord[ind][1], text=road_map[ind][1],
                 tag=None, state=NORMAL, anchor=W)

        # generate distances
        text_gen(canv, dist_coord_x, dist_coord_y, text=distances[ind - 1], tag=distance_tag[ind - 1],
                 state=HIDDEN, anchor=None)
        text_gen(canv_scroll, scroll_width / 2, linear_coord[ind][1] - (size_scroll_coord / 2),
                 text=distances[ind], tag=distance_tag[ind - 1], state=NORMAL, anchor=W)
        ind = (ind + 1) % ln

    # generate ovals on map
    oval_button_gen(canv, canv, ln, road_map, func=get_circle_coordinates, tag_1=city_tag,
                    tag_2=distance_tag, index_1=2, index_2=3)

    oval_button_gen(canv_scroll, canv, ln, linear_coord, func=get_circle_coordinates, tag_1=city_tag,
                    tag_2=distance_tag, index_1=0, index_2=1)

    window.mainloop()
