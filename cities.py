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
    with open(file_name, "r") as f:  # 'with' handles files without the need for closing
        road_map = [(tuple(line.split('\t'))) for line in f]  # adds tuples of lines to road_map list
    format_check_prune(road_map)  # checks for duplicates and format errors - deletes 'bad' lines
    if len(road_map) <= 1:  # allows main() to check for the absence of cities (lines) in road map file
        return False
    return road_map


def remove_blank(road_map, line):
    if '\n' in line:
        road_map.remove(line)


def remove_duplicates(road_map):
    """
    removes duplicate tuples from road_map
    problem: error occurs because the removal of an item reduces the length of road_map
    """
    return list(set(road_map))

def try_except_remove(line, road_map):
    """
    evaluates tuples for format: 'string, string, float, float'
    change this so it catches format errors
    """
    try:
        str(line[0])
        str(line[1])
        float(line[2])
        float(line[3])
    except ValueError:
        road_map.remove(line)
    except IndexError:
        road_map.remove(line)


def format_check_prune(road_map):
    """
    checks and prunes road_map for errors: duplicates, wrong format
    """
    [try_except_remove(line, road_map) for line in road_map]
    remove_duplicates(road_map)
    [remove_blank(road_map, line) for line in road_map]
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


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    try:
        enter_file_name_here = 'city-data.txt'
        if enter_file_name_here.endswith('.txt'):
            if read_cities(enter_file_name_here):
                road_map = read_cities(enter_file_name_here)
                print('Initial road_map: ')
                print_cities(road_map)
                print('Total distance: ', compute_total_distance(road_map), '\n')
                new_road_map = find_best_cycle(road_map)
                print('New road map: ')
                print_cities(new_road_map)
                print('Total distance : ', compute_total_distance(new_road_map), '\n')
                print('Cities and their connections: ')
                print_map(new_road_map)
                visualise(new_road_map)
            else:
                print('Cannot calculate distance, choose a file containing one or more cities')
        else:
            print('File is the wrong format: enter a .txt file')
    except FileNotFoundError:
        print("No file found: please enter the name of a file that exists within main's directory.")


if __name__ == "__main__":  # keep this in
    main()
