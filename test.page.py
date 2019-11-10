import math

road_map1 = [("Minnesota", 44.95, -93.094, "Saint Paul"),
             ("Minnesota", "Saint Paul", 44.95, -93.094),
             ("Kentucky", "Frankfort", 38.197274, -84.86311),
             ("Delaware", "Dover", 39.161921, -75.526755),
             ("Minnesota", "Saint Paul", 44.95, -93.094),
             ("Delaware", "Dover", 39.161921, -75.526755, 123123),
             ("Minnesota", 44.95, -93.094, "Saint Paul")]


def remove_duplicates(road_map):
    road_map.sort()
    [road_map.remove(road_map[line]) for line in range(len(road_map) - 1) if road_map[line] == road_map[line + 1]]


def format_check_prune(road_map):
    '''
    checks and prunes road_map format errors
    '''
    [try_except_remove(line, road_map) for line in road_map]
    remove_duplicates(road_map)
    [road_map.remove(line) for line in road_map if len(line) > 4 or len(line) < 4]


def try_except_remove(line, road_map):
    try:
        str(line[0])
        str(line[1])
        float(line[2])
        float(line[3])
    except ValueError:
        road_map.remove(line)

format_check_prune(road_map1)
print(road_map1)