import math

road_map1 = [("Minnesota", 44.95, -93.094, "Saint Paul"),
             ("Minnesota", "Saint Paul", 44.95, -93.094),
             ("Kentucky", "Frankfort", 38.197274, -84.86311),
             ("Delaware", "Dover", 39.161921, -75.526755),
             ("Minnesota", "Saint Paul", 44.95, -93.094),
             ("Delaware", "Dover", 39.161921, -75.526755, 123123),
             ("Minnesota", 44.95, -93.094, "Saint Paul")]


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

swap_cities()