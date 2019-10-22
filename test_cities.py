import pytest
from cities import *


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                ("Delaware", "Dover", 39.161921, -75.526755),
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    assert compute_total_distance(road_map1) == pytest.approx(9.386+18.496+10.646, 0.01)


    '''add your further tests'''

def test_swap_cities():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]
    index1 = 0
    index2 = 1
    assert swap_cities(road_map1, index1, index2) == [("Delaware", "Dover", 39.161921, -75.526755),
                                                      ("Kentucky", "Frankfort", 38.197274, -84.86311),
                                                      ("Minnesota", "Saint Paul", 44.95, -93.094)]

    '''add your tests'''

def test_shift_cities():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]

    assert shift_cities(road_map1) == [("Delaware", "Dover", 39.161921, -75.526755),
                                       ("Kentucky", "Frankfort", 38.197274, -84.86311),
                                       ("Minnesota", "Saint Paul", 44.95, -93.094)]



    '''add your tests'''

