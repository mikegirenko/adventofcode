from adventofcode.toboggan_trajectory.toboggan_trajectory import *


def test_count_trees():
    map_to_traverse = read_map()
    assert count_trees(map_to_traverse) == 7
