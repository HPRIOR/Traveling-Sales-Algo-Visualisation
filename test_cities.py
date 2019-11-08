import pytest
from cities import *

'''
make tests for road maps with 1 item or 0 
'''


def test_compute_individual_distance():
    pass


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]

    # calculate this by hand then and give value at the end
    assert compute_total_distance(road_map1) == pytest.approx(38.52, 0.1)


def test_swap_cities():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]

    road_map2 = []

    road_map_3 = [("Kentucky", "Frankfort", 38.197274, -84.86311)]

    assert swap_cities(road_map1, 0, 1) == ([("Delaware", "Dover", 39.161921, -75.526755),
                                             ("Kentucky", "Frankfort", 38.197274, -84.86311),
                                             ("Minnesota", "Saint Paul", 44.95, -93.094)], pytest.approx(38.52, 0.1))
    assert swap_cities(road_map1, 1, 1) == ([("Delaware", "Dover", 39.161921, -75.526755),
                                             ("Kentucky", "Frankfort", 38.197274, -84.86311),
                                             ("Minnesota", "Saint Paul", 44.95, -93.094)], pytest.approx(38.52, 0.1))
    assert swap_cities(road_map1, 1, 0) == ([("Kentucky", "Frankfort", 38.197274, -84.86311),
                                             ("Delaware", "Dover", 39.161921, -75.526755),
                                             ("Minnesota", "Saint Paul", 44.95, -93.094)], pytest.approx(38.52, 0.1))

    ## assert swap_cities(road_map2, 0, 1) == IndexError
    # tests for road map with just 1 or 0 results?


def test_shift_cities():
    # tests for road map with just 1 or 0 results?
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]

    assert shift_cities(road_map1) == [("Minnesota", "Saint Paul", 44.95, -93.094),
                                       ("Kentucky", "Frankfort", 38.197274, -84.86311),
                                       ("Delaware", "Dover", 39.161921, -75.526755)]
