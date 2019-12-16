# import relevant modules, not everything
import random
import math
from tkinter import *
from visualiser import *


def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 

      [(state, city, latitude, longitude), ...] 

    Use this as your initial `road_map`, that is, the cycle 

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.

    """
    with open(file_name, "r") as f:                             # 'with' handles files without the need for closing
        road_map = [(tuple(line.split('\t'))) for line in f]    # adds tuples of lines to road_map list
    format_check_prune(road_map)                                # checks for duplicates and format errors - deletes 'bad' lines
    if len(road_map) == 0:                                      # allows main() to check for the absence of cities (lines) in road map file
        return False
    return road_map


def remove_duplicates(road_map):
    """
    removes duplicate tuples from road_map
    """
    road_map.sort()
    [road_map.remove(road_map[line]) for line in range(len(road_map) - 1) if road_map[line] == road_map[line + 1]]


def try_except_remove(line, road_map):
    """
    evaluates tuples for format: 'string, string, float, float'
    """
    try:
        str(line[0])
        str(line[1])
        float(line[2])
        float(line[3])
    except ValueError:
        road_map.remove(line)
    # maybe do this without converting types


def format_check_prune(road_map):
    '''
    checks and prunes road_map for errors: duplicates, wrong format
    '''
    [try_except_remove(line, road_map) for line in road_map]
    remove_duplicates(road_map)
    [road_map.remove(line) for line in road_map if len(line) > 4 or len(line) < 4]


def print_formatter(tple):
    """
    :param: takes in a tuple with the format: string, string, float, float
    :return: tuple with city, x, y (to two decimal places)
    """
    tple = list(tple)
    tple.pop(0)
    tple[1] = '%.2f' % float(tple[1])
    tple[2] = '%.2f' % float(tple[2])
    return tuple(tple)
    # add tests


def print_cities(road_map):
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
    print([print_formatter(x) for x in road_map])


def compute_individual_distance(x1, y1, x2, y2):
    """
    returns distance between two coordinates
    """
    return math.sqrt(((float(x1) - float(x2)) ** 2) + ((float(y1) - float(y2)) ** 2))
    # add test


def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    ln = len(road_map)
    ind = 0
    total = 0
    for i in range(ln):
        total += compute_individual_distance(road_map[ind - 1][2],
                                             road_map[ind - 1][3],
                                             road_map[ind][2],
                                             road_map[ind][3])
        ind = (ind + 1) % ln
    return total


def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    if index1 == index2:
        return road_map, compute_total_distance(road_map)
    else:
        road_map[index1], road_map[index2] = road_map[index2], road_map[index1]
        return road_map, compute_total_distance(road_map)


def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """
    road_map.insert(0, road_map[-1])
    del road_map[-1]
    return road_map


def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    best_total = compute_total_distance(road_map)
    best_road_map = road_map
    for i in range(10000):
        index1, index2 = int((len(road_map) * random.random())), int((len(road_map) * random.random()))
        swap = swap_cities(shift_cities(road_map), index1, index2)
        if swap[1] < best_total:
            best_total = swap[1]
            best_road_map = swap[0][:]
    return best_road_map


def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and
    their connections, along with the cost for each connection
    and the total cost.
    """
    ln = len(road_map)
    loop_distance = 0

    for i in range(1, ln):
        distance = compute_individual_distance(road_map[i - 1][2], road_map[i - 1][3], road_map[i][2], road_map[i][3])
        print('     The distance from %s to %s is %.2f' % (road_map[i - 1][1], road_map[i][1], distance))
        loop_distance += distance

    last_first_distance = compute_individual_distance(road_map[-1][2], road_map[- 1][3], road_map[0][2], road_map[0][3])
    print('     The distance from %s to %s is %.2f' % (road_map[-1][1], road_map[0][1], last_first_distance))
    total = loop_distance + last_first_distance
    print('     The total distance travelled will be roughly %.2f' % total)


def visualise(road_map):
    ln = len(road_map)  # length needed for functions below

    # geometry variables defined so that changes will effect whole window
    canvas_height, canvas_width = 825, 1350
    bottom_height = 100
    scroll_width = 200
    divider_width = 2
    window_width = canvas_width + scroll_width + divider_width
    bottom_width = (window_width / 2)
    size_scroll_coord = 100

    # get numbers list to use in linear coords
    linear_coord = linear_coord_list(40, size_scroll_coord, ln, int(scroll_width / 2.5))
    scroll_distance = linear_coord[-1][1] + 30

    # get info prior to normalisation
    distances = distances_list(road_map)

    # normalise data
    road_map = change_visualise_data(road_map, canvas_width, canvas_height, c_edge=2)

    # create main tk window
    window = Tk()
    window.title('Traveling salesperson app')
    window.geometry('+100+0')
    window.resizable(FALSE, FALSE)

    # create frames
    top_frame = Frame(window, width=window_width, height=canvas_height)

    divide_canvas = Frame(window, width=window_width, height=divider_width, bg='black')
    bottom_frame = Frame(window, width=window_width, height=bottom_height)

    info_frame_1 = Frame(bottom_frame, width=bottom_width, height=bottom_height, bg='gray89')
    divide_inpinf = Frame(bottom_frame, width=divider_width, height=bottom_height, bg='black')
    info_frame_2 = Frame(bottom_frame, width=bottom_width, height=bottom_height, bg='gray89')

    canvas_frame = Frame(top_frame, width=canvas_width, height=canvas_height, bg='gray89')
    scroll_frame = Frame(top_frame)
    scroll_frame_divider = Frame(top_frame, width=divider_width, height=canvas_height, bg='black')

    scrollbar = Scrollbar(scroll_frame)

    # organise frames
    canvas_frame.grid(row=0, column=0)
    divide_canvas.grid(row=1, column=0)
    bottom_frame.grid(row=2, column=0)
    info_frame_1.grid(row=0, column=0)
    divide_inpinf.grid(row=0, column=1)
    info_frame_2.grid(row=0, column=2)
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
    start(canv, road_map)

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
        text_gen(canv, road_map[ind - 1][2], (road_map[ind - 1][3] - 5), text=road_map[ind - 1][0],
                 tag=city_tag[ind - 1], state=HIDDEN, anchor=S)
        text_gen(canv_scroll, scroll_width / 2, linear_coord[ind][1], text=road_map[ind][0],
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

    # info pane


    window.mainloop()


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    enter_file_name_here = 'city-data.txt'
    if read_cities(enter_file_name_here):
        road_map = read_cities(enter_file_name_here)
        print_cities(road_map)
        print('total distance: ', compute_total_distance(road_map))
        new_road_map = find_best_cycle(road_map)
        print('new road map: ', new_road_map)
        print('best calculated total distance : ', compute_total_distance(new_road_map))
        print('Cities and their connections in an easily understandable format: ')
        print_map(new_road_map)
        visualise(new_road_map)

    else:
        print('Cannot calculate distance, input one or more cities')


if __name__ == "__main__":  # keep this in
    main()
