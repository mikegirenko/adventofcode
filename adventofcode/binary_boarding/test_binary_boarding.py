from adventofcode.binary_boarding.binary_boarding import *


def test_puzzle_input():
    puzzle_input = read_puzzle_input()
    assert puzzle_input


def test_find_row():
    boarding_pass = "FBFBBFFRLR"
    row = find_row(boarding_pass)
    assert row == 44


"""
For example, consider just the first seven characters of FBFBBFFRLR:
Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63. x
B means to take the upper half, keeping rows 32 through 63. x
F means to take the lower half, keeping rows 32 through 47. x
B means to take the upper half, keeping rows 40 through 47. x
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.
"""