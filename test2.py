from tkinter import *
from cities import *

road_map = read_cities('test-city-data.txt')


def oval_button_gen(canvas, ln, road_map, distance_tags, city_tags):
    """
    Ovals used as 'buttons' to reveal information
    Binding events to canvas objects requires a variable to identify
        canvas object, hence i = canvas... in loop
    For each oval object, 'Leave' and 'Enter' events are created which correspond to map data
    """
    ind = 0
    for i in range(ln):
        i = canvas.create_oval(get_circle_coordinates(road_map[ind]), fill='green', activefill='red')

        canvas.tag_bind(i, '<Enter>', lambda_func(canvas, f=show, lst=city_tags, index=ind, ln=ln))
        canvas.tag_bind(i, '<Leave>', lambda_func(canvas, f=hide, lst=city_tags, index=ind, ln=ln))

        ind = (ind + 1) % ln


def lambda_func(canvas, f, lst, index, ln):
    """
    this was needed because the ordinary lambda functions in circle_button_gen would
    not update their indices, which are required to match generate tag identifiers
    HO function allow for the use of both 'leave' and 'enter' function
    """
    return lambda e: f(e, canvas, lst[index], ln)


def raise_lower_tag(tag):
    """
    gives the tags above and below input tag
    """
    if len(tag) < 3:
        tag_minus, tag_plus = int(tag[1]) - 1, int(tag[1]) + 1
        tag_below, tag_above = tag[0] + str(tag_minus), tag[0] + str(tag_plus)
        return tag_below, tag_above
    else:
        tag_minus, tag_plus = int(tag[1:]) - 1, int(tag[1:]) + 1
        tag_below, tag_above = tag[0] + str(tag_minus), tag[0] + str(tag_plus)
        return tag_below, tag_above
    # I think i could encapsulate the control statements for hide and show here


def hide(event, canvas, tag, ln):
    """
    Hides object on canvas with given tag
    """
    # if on the last city: make the next tag the first city
    if tag == 'C' + str(ln - 1):
        canvas.itemconfigure(tag, state=HIDDEN)
        canvas.itemconfigure('C0', state=HIDDEN)
        canvas.itemconfigure(raise_lower_tag(tag)[0], state=HIDDEN)
    # if on the first city: make the previous tag the first city
    elif tag == 'C0':
        canvas.itemconfigure(tag, state=HIDDEN)
        canvas.itemconfigure('C' + str(ln - 1), state=HIDDEN)
        canvas.itemconfigure(raise_lower_tag(tag)[1], state=HIDDEN)
    elif int(tag[1]) != 0:
        canvas.itemconfigure(tag, state=HIDDEN)
        canvas.itemconfigure(raise_lower_tag(tag)[0], state=HIDDEN)
        canvas.itemconfigure(raise_lower_tag(tag)[1], state=HIDDEN)


def show(event, canvas, tag, ln):
    """
    Shows object on canvas with given tag
    """
    # if on the last city: make the next tag the first city
    if tag == 'C' + str(ln - 1):
        canvas.itemconfigure(tag, state=NORMAL)
        canvas.itemconfigure('C0', state=NORMAL)
        canvas.itemconfigure(raise_lower_tag(tag)[0], state=NORMAL)
    elif tag == 'C0':
        # if on the first city: make the previous tag the first city
        canvas.itemconfigure(tag, state=NORMAL)
        canvas.itemconfigure('C' + str(ln - 1), state=NORMAL)
        canvas.itemconfigure(raise_lower_tag(tag)[1], state=NORMAL)
    elif int(tag[1]) != 0:
        canvas.itemconfigure(tag, state=NORMAL)
        canvas.itemconfigure(raise_lower_tag(tag)[0], state=NORMAL)
        canvas.itemconfigure(raise_lower_tag(tag)[1], state=NORMAL)


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

def distance_text_gen(canvas, x, y, text, tag):
    """
    Generate text between two coordinates, with tag identifier
    """
    # coordinates in the middle of line
    pass


def line_gen(canvas, x1, y1, x2, y2):
    """
    Generates lines between two coordinates
    """
    canvas.create_line(x1, y1, x2, y2, arrow=LAST, fill='blue')


def start(canvas, road_map):
    canvas.create_line(road_map[0][2], road_map[0][3], road_map[0][2], 20, fill='red')
    canvas.create_text(road_map[0][2], 10, text='Start', fill='red')


def get_circle_coordinates(line):
    """
    line input format: str,str,float(x),float(y)
    returns x1,y1,x2,y2 from x,y where xn/yn +- 5; needed to circle coordinates
    """
    circ_size = 4
    x = line[2]
    y = line[3]
    x1, y1, x2, y2 = (x + circ_size), (y + circ_size), (x - circ_size), (y - circ_size)
    return x1, y1, x2, y2


def func_index_list(f, i, lst):
    """
    applies a function to all the indexes within a nested loop (e.g. all the 1st items in a matrix)
    used to find the minimum and maximum values of coordinates in a nested list (change_v_data)
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
        distance_list.append(compute_individual_distance(road_map[ind - 1][2],
                                                         road_map[ind - 1][3],
                                                         road_map[ind][2],
                                                         road_map[ind][3]))
        ind = (ind + 1) % ln
    return distance_list


def visualise(road_map):
    canvas_size_x = 1500
    canvas_size_y = 825

    # get info prior to normalisation
    prior_compute = compute_total_distance(road_map)
    distances = distances_list(road_map)
    best_cycle = find_best_cycle(road_map)
    post_compute = compute_total_distance(best_cycle)

    # normalise data
    road_map = change_visualise_data(best_cycle, canvas_size_x, canvas_size_y, c_edge=2)

    # create main tk window
    window = Tk()
    window.title('Traveling salesperson app')
    window.geometry('+100+0')
    window.resizable(FALSE, FALSE)

    # create frames
    canvas_frame = Frame(window, width=canvas_size_x, height=canvas_size_y, bg='gray89')
    divide_canvas = Frame(window, width=1500, height=2, bg='black')
    bottom_frame = Frame(window, width=1500, height=200)
    input_frame = Frame(bottom_frame, width=749, height=100, bg='gray89')
    divide_inpinf = Frame(bottom_frame, width=2, height=100, bg='black')
    info_frame = Frame(bottom_frame, width=749, height=100, bg='gray89')

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

    ln = len(road_map)  # length needed for functions below

    # create tags to identify text
    distance_tag = tag_gen(ln, 'D')
    city_tag = tag_gen(ln, 'C')

    # create start and finish indicators
    start(canv, road_map)

    # create lines
    ind = 0
    for i in range(ln):
        # generate lines
        line_gen(canv, road_map[ind - 1][2], road_map[ind - 1][3], road_map[ind][2], road_map[ind][3])
        # generate city text
        text_gen(canv, road_map[ind - 1][2], (road_map[ind - 1][3] - 5), text=road_map[ind - 1][0], tag=city_tag[ind - 1],
                 state=HIDDEN, anchor=S)

        # generate distances

        ind = (ind + 1) % ln

    oval_button_gen(canv, ln, road_map, distance_tag, city_tags=city_tag)
    window.mainloop()


visualise(road_map)
