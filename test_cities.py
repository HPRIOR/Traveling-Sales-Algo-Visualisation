import pytest
from cities import *


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
    index1 = 0
    index2 = 1
    assert swap_cities(road_map1, index1, index2) == [("Delaware", "Dover", 39.161921, -75.526755),
                                                      ("Kentucky", "Frankfort", 38.197274, -84.86311),
                                                      ("Minnesota", "Saint Paul", 44.95, -93.094)]


def test_shift_cities():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]

    assert shift_cities(road_map1) == [("Minnesota", "Saint Paul", 44.95, -93.094),
                                       ("Delaware", "Dover", 39.161921, -75.526755),
                                       ("Kentucky", "Frankfort", 38.197274, -84.86311)]













