def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return
    them as a list of four-tuples:

      [(state, city, latitude, longitude), ...]

    Use this as your initial `road_map`, that is, the cycle

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.

    """
    with open(file_name, "r") as f:  # 'with' handles files without the need for closing
        road_map = [(tuple(line.split('\t'))) for line in f]  # adds tuples of lines to road_map list
    format_check_prune(road_map)  # checks for duplicates and format errors - deletes 'bad' lines
    if len(road_map) <= 1:  # allows main() to check for the absence of cities (lines) in road map file
        return False
    return road_map

def remove_blank(road_map, line):
    if '\n' in line:
        road_map.remove(line)

def remove_duplicates(road_map):
    """
    removes duplicate tuples from road_map
    problem: error occurs because the removal of an item reduces the length of road_map
    """
    return list(set(road_map))

def try_except_remove(line, road_map):
    """
    evaluates tuples for format: 'string, string, float, float'
    """
    try:
        str(line[0])
        str(line[1])
        float(line[2])
        float(line[3])
    except ValueError:
        road_map.remove(line)
    except IndexError:
        road_map.remove(line)

    # maybe do this without converting types
    # doesn't remove single string characters
    # maybe try the same thing but return true or false values so that format check prune can do the work


def format_check_prune(road_map):
    """
    checks and prunes road_map for errors: duplicates, wrong format
    """
    [try_except_remove(line, road_map) for line in road_map]
    remove_duplicates(road_map)
    [remove_blank(road_map, line) for line in road_map]
    [road_map.remove(line) for line in road_map if len(line) > 4 or len(line) < 4]


rm = read_cities('file.txt')
print(rm)