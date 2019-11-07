import math
from itertools import cycle

"""
def read_cities(file_name):
    road_map = []
    with open(file_name, "r") as f:
        for line in f:
            road_map.append(tuple(line.split('\t')))
    return road_map



def print_cities(road_map):
    road_map_print = []
    for cities in road_map:
        road_map_print.append(list(cities))
    for cities in road_map_print:
        cities.pop(0)
        cities[1] = '%.2f' % float(cities[1])
        cities[2] = '%.2f' % float(cities[2])
    print(road_map_print)



def calculate(road_map):
    x = road_map[i-1]
    for i in range(len(road_map)):
        print(road_map[i])


calculate(read_cities('city-data.txt'))


road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                ("Delaware", "Dover", 39.161921, -75.526755),
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

ln = len(road_map)

loop_result = 0
for i in range(1, ln):
    x1 = road_map[i - 1][2]
    y1 = road_map[i - 1][3]
    x2 = road_map[i][2]
    y2 = road_map[i][3]
    loop_result += (math.sqrt(((x1-x2)**2)+((y1 - y2)**2)))

x1_start = road_map[0][2]
y1_start = road_map[0][3]
x2_end = road_map[ln-1][2]
y2_end = road_map[ln-1][3]

start_end = (math.sqrt(((x1_start-x2_end)**2)+((y1_start - y2_end)**2)))

result = loop_result + start_end

print(result)



road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
             ("Delaware", "Dover", 39.161921, -75.526755),
             ("Minnesota", "Saint Paul", 44.95, -93.094)]


def compute_individual_distance(x1, y1, x2, y2):
    return math.sqrt(((float(x1) - float(x2)) ** 2) + ((float(y1) - float(y2)) ** 2))


def compute_total_distance(road_map):
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


print(compute_total_distance(road_map1))

"""