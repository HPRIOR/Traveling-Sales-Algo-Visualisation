def read_cities(file_name):
    road_map = []
    f = open(file_name, "r")
    for line in f:
        road_map.append(tuple(line.split('	')))
    f.close()
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


print_cities(read_cities('city-data.txt'))
