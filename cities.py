# import relevant modules, not everything
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
    format_check_prune(road_map)  # checks and prunes road_map format errors
    return road_map


def format_check_prune(road_map):
    for line in road_map:
        if len(line) > 4 or len(line) < 4:
            road_map.remove(line)
    for line in road_map:
        try:
            str(line[0])
            str(line[1])
            float(line[2])
            float(line[3])
        except ValueError:
            road_map.remove(line)

    # add test for this function


def print_formatter(tple):
    """
    :param: takes in a tuple with the format: string, string, float, float
    :return: tuple with city, x,y to two decimal points
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
    road_map_print = [print_formatter(x) for x in road_map]
    print(road_map_print)


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

    # within the loop check for bad result with try, except, raise errors, and output amount of errors
    # remove bad lines from file # how to handle single or empty road_maps


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
        swap = road_map[index1]
        road_map[index1] = road_map[index2]
        road_map[index2] = swap
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
        index = (int((len(road_map) * random.random())), int((len(road_map) * random.random())))
        swap = swap_cities(shift_cities(road_map), index[0], index[1])
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
    ind = 0
    for i in range(1, ln):

        print('Journey', (ind + 1), ': ')
        print('     Between', road_map[ind][1], 'and', road_map[ind - 1][1])
        print('     Distance: ', compute_individual_distance(road_map[ind - 1][2],
                                                             road_map[ind - 1][3],
                                                             road_map[ind][2],
                                                             road_map[ind][3]))
        ind = (ind + 1) % ln


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    road_map = read_cities('city-data.txt')
    print_cities(road_map)
    print('total distance: ', compute_total_distance(road_map))
    new_road_map = find_best_cycle(road_map)
    print_cities(new_road_map)
    print('best calculated total distance : ', compute_total_distance(new_road_map))
    # print_map(new_road_map)


if __name__ == "__main__":  # keep this in
    main()
