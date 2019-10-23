def read_cities(file_name):
    road_map = []
    f = open(file_name, "r")
    for line in f:
        t = line.split()
        road_map.append(tuple(t))
    f.close()
    return road_map



print(read_cities('city-data.txt'))