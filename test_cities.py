import pytest
from cities import *


# at least 5 for each
def test_print_formatter():
    """
    Happy for the function to produce an Index error when given the wrong format;
    this shouldn't happen due to previous function 'format_check_prune'
    """
    tuple_1 = ("test", "me", 1.22, 1.42)
    tuple_2 = ("test2", 4.20, 1.2)
    tuple_3 = (1.2, "test3", 4.20)
    assert print_formatter(tuple_1) == ("me", '1.22', '1.42')
    with pytest.raises(IndexError):
        print_formatter(tuple_2)
        print_formatter(tuple_3)


def test_tag_gen():
    assert tag_gen(3, "A") == ["A0", "A1", "A2"]
    assert tag_gen(2, "A") == ["A0", "A1"]
    assert tag_gen(0, "A") == []
    assert tag_gen(1, "ZZ") == ["ZZ0"]
    assert tag_gen(1, "ZZgfd") == ["ZZgfd0"]


def test_raise_lower_tag():
    pass


def test_get_mid_coord():
    assert get_mid_coord(1, 1, 2, 2) == (1.5, 1.5)
    assert get_mid_coord(1.3, 1.3, 2.1, 2.1) == (pytest.approx(1.7, 0.1), pytest.approx(1.7, 0.1))
    assert get_mid_coord(100, 120, 2300, 2200) == (1200, 1160)
    assert get_mid_coord(1.32, 12.32, 20.23, 101.12) == (10.775, 56.72)
    assert get_mid_coord(-100, -120, 2300, 2200) == (1100, 1040)
    assert get_mid_coord(-1, -2, -3, -4) == (-2, -3)


def test_compute_individual_distance():
    assert compute_individual_distance(1, 2, 3, 4) == pytest.approx(2.928, 0.1)
    assert compute_individual_distance(1.5, 2.5, 3.5, 4.5) == pytest.approx(2.828, 0.1)
    assert compute_individual_distance(4, 3, 2, 1) == pytest.approx(2.928, 0.1)
    assert compute_individual_distance(3, 1, 2, 4) == pytest.approx(3.162, 0.1)
    assert compute_individual_distance(-1, -2, -3, -4) == pytest.approx(2.828, 0.1)


def test_func_index_list():
    test_list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert func_index_list(min, 0, test_list1) == 1
    assert func_index_list(min, 1, test_list1) == 2
    assert func_index_list(min, 2, test_list1) == 3
    assert func_index_list(max, 0, test_list1) == 7
    assert func_index_list(max, 1, test_list1) == 8
    assert func_index_list(max, 2, test_list1) == 9


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]
    road_map2 = [("test", "test", 10, 20),
                 ("test", "test", 20, 30),
                 ("test", "test", 30, 40)]
    road_map3 = [("test", "test", -10, -20),
                 ("test", "test", -20, -30),
                 ("test", "test", -30, -40)]
    road_map4 = [("test", "test", -10, 20),
                 ("test", "test", -20, 30),
                 ("test", "test", -30, 40)]
    road_map5 = [("test", "test", -10, 20),
                 ("test", "test", -20, -30),
                 ("test", "test", -30, 40)]

    assert compute_total_distance(road_map1) == pytest.approx(38.52, 0.1)
    assert compute_total_distance(road_map2) == pytest.approx(56.56, 0.1)
    assert compute_total_distance(road_map3) == pytest.approx(56.56, 0.1)
    assert compute_total_distance(road_map4) == pytest.approx(56.56, 0.1)
    assert compute_total_distance(road_map5) == pytest.approx(56.56, 0.1)

    # finish 4 and 5


def test_distances_list():
    pass


def test_swap_cities():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]
    road_map2 = []
    road_map3 = [("Kentucky", "Frankfort", 38.197274, -84.86311)]

    assert swap_cities(road_map1, 0, 1) == ([("Delaware", "Dover", 39.161921, -75.526755),
                                             ("Kentucky", "Frankfort", 38.197274, -84.86311),
                                             ("Minnesota", "Saint Paul", 44.95, -93.094)], pytest.approx(38.52, 0.1))
    assert swap_cities(road_map1, 1, 1) == ([("Delaware", "Dover", 39.161921, -75.526755),
                                             ("Kentucky", "Frankfort", 38.197274, -84.86311),
                                             ("Minnesota", "Saint Paul", 44.95, -93.094)], pytest.approx(38.52, 0.1))
    assert swap_cities(road_map1, 1, 0) == ([("Kentucky", "Frankfort", 38.197274, -84.86311),
                                             ("Delaware", "Dover", 39.161921, -75.526755),
                                             ("Minnesota", "Saint Paul", 44.95, -93.094)], pytest.approx(38.52, 0.1))
    assert swap_cities(road_map3, 0, 0) == ([("Kentucky", "Frankfort", 38.197274, -84.86311)], pytest.approx(0.0, 0.1))

    with pytest.raises(IndexError):
        swap_cities(road_map1, 0, 4)
        swap_cities(road_map2, 0, 1)
        swap_cities(road_map3, 0, 1)


def test_shift_cities():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]
    road_map2 = [("Kentucky", "Frankfort", 38.197274, -84.86311)]
    road_map3 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755)]
    road_map4 = []

    assert shift_cities(road_map1) == [("Minnesota", "Saint Paul", 44.95, -93.094),
                                       ("Kentucky", "Frankfort", 38.197274, -84.86311),
                                       ("Delaware", "Dover", 39.161921, -75.526755)]
    assert shift_cities(road_map2) == [("Kentucky", "Frankfort", 38.197274, -84.86311)]
    assert shift_cities(road_map3) == [("Delaware", "Dover", 39.161921, -75.526755),
                                       ("Kentucky", "Frankfort", 38.197274, -84.86311)]
    with pytest.raises(IndexError):
        shift_cities(road_map4)
