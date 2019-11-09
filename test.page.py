import math


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


def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and
    their connections, along with the cost for each connection
    and the total cost.
    """
    p_map = [print_formatter(x) for x in road_map]
    ln = len(p_map)
    loop_distance = 0
    for i in range(1, ln):
        distance = compute_individual_distance(p_map[i-1][1], p_map[i][1], p_map[i-1][2], p_map[i][2])
        print('The distance from %s to %s is %f.2' % (p_map[i-1][0], p_map[i][0], distance))
        loop_distance += distance
    last_first_distance = compute_individual_distance(p_map[-1][1], p_map[0][1], p_map[-1][2], p_map[0][2])
    print('The distance from %s to %s is %f.2' % (p_map[-1][0], p_map[0][0], last_first_distance))
    total = loop_distance + last_first_distance
    print('The total distance travelled will be %.2f' % total)




    # here the distance between 0 - -1 =
    # then the total distance


def print_formatter(tple):
    """
    :param takes in a tuple from road_map
    :return: tuple with city, x,y to two decimal points
    """
    tple = list(tple)
    tple.pop(0)
    tple[1] = '%.2f' % float(tple[1])
    tple[2] = '%.2f' % float(tple[2])
    return tuple(tple)


road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
             ("Delaware", "Dover", 39.161921, -75.526755),
             ("Minnesota", "Saint Paul", 44.95, -93.094)]

print_map(road_map1)
