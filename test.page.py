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


    #sqrt((x1-x2)^2 + (y1-y2)^2)

'''
If you want to treat a list  as circular(the first item follows the last item), the item  
after lst[i] is not just lst(i + 1), but is lst[(i + 1) % len(lst)].
'''


