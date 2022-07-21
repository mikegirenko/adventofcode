# https://adventofcode.com/2020/day/3
from typing import List


def read_map() -> List[str]:
    with open("map.txt", "r") as file:
        read_data = file.read()
    file_lines = read_data.split("\n")

    return file_lines


def count_trees(a_map) -> int:
    map_to_traverse = a_map
    i = 1
    trees_counter = 0
    while i < len(map_to_traverse): # skip first line in the map because "down 1"
        ind = 3 * i
        ch = map_to_traverse[i][ind]  # this is to do "right 3"
        if ch == "#":
            trees_counter += 1
        i += 1

    return trees_counter
