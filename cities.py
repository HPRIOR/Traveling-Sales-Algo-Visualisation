# import relevant modules, not everything
from tkinter import *
import random
import math


def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 

      [(state, city, latitude, longitude), ...] 

    Use this as your initial `road_map`, that is, the cycle 

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.

    """
    with open(file_name, "r") as f:  # 'with' handles files without the need for closing
        road_map = [(tuple(line.split('\t'))) for line in f]  # adds tuples of lines to road_map list
    format_check_prune(road_map)  # checks for duplicates and format errors - deletes bad lines
    if len(road_map) == 0:  # allows main() to check for the absence of cities (lines) in road map file
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
        print('The distance from %s to %s is %.2f' % (road_map[i - 1][1], road_map[i][1], distance))
        loop_distance += distance

    last_first_distance = compute_individual_distance(road_map[-1][2], road_map[- 1][3], road_map[0][2], road_map[0][3])
    print('The distance from %s to %s is %.2f' % (road_map[-1][1], road_map[0][1], last_first_distance))
    total = loop_distance + last_first_distance
    print('The total distance travelled will be roughly %.2f' % total)


def change_visualise_data(road_map, canvas_max_size_x, canvas_max_size_y):
    """
    returns normalised data for visualisation function
    format of return: state, city, x(float), y(float)
    """

    data_road_map = []
    [data_road_map.append(list(line)) for line in road_map]
    c_edge = 3

    # removes minus values
    for line in data_road_map:
        line[2] = (float(line[2]) + 90)  # x
        line[3] = (float(line[3]) + 180)  # y

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
    return data_road_map


def get_circle_coordinates(line):
    """
    line input format: str,str,float(x),float(y)
    returns x1,y1,x2,y2 from x,y where xn/yn +- 5; needed to circle coordinates
    """
    circ_size = 2.5
    x = line[2]
    y = line[3]
    x1, y1 = (x + circ_size), (y + circ_size)
    x2, y2 = (x - circ_size), (y - circ_size)
    return x1, y1, x2, y2


def func_index_list(f, i, lst):
    """
    applies a function to all the indexes within a nested loop (e.g. all the 1st items in a matrix)
    used to find the minimum and maximum values of coordinates in a nested list
    """
    new_list = []
    [new_list.append(float(line[i])) for line in lst]
    func = f(new_list)
    return func


def visualise(road_map):
    canvas_size_x = 1000
    canvas_size_y = 600
    prior_compute = compute_total_distance(road_map)
    road_map = change_visualise_data(road_map, canvas_size_x, canvas_size_y)


    main_win = Tk()

    lab = Label(main_win, text='the total distance is: %f' % prior_compute)
    lab.pack()

    canv = Canvas(main_win, height=canvas_size_y, width=canvas_size_x)
    canv.pack()

    # visualising road_map
    ln = len(road_map)
    ind = 0
    for i in range(ln):
        # dots for cities
        canv.create_oval(get_circle_coordinates(road_map[ind]))
        # text
        canv.create_text(road_map[ind][2], road_map[ind][3], text=road_map[ind][1], anchor=N, fill='red')
        # lines between cities
        canv.create_line(road_map[ind - 1][2], road_map[ind - 1][3],
                         road_map[ind][2], road_map[ind][3], arrow=LAST)
        ind = (ind + 1) % ln

    main_win.mainloop()


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
        visualise(new_road_map)
    else:
        print('Cannot calculate distance, input one or more cities')


if __name__ == "__main__":  # keep this in
    main()
