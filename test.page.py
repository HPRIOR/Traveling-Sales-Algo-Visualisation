import math

road_map1 = [("Kentucky", "Frankfort", '38.197274', '-84.86311', 'asdasdasd'),
             ("Delaware", "Dover", '39.161921', '-75.526755'),
             ("Minnesota", "Saint Paul", '44.95'),
             ("Minnesota", '44.95', '-93.094', "Saint Paul")]


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


format_check_prune(road_map1)

print(road_map1)
