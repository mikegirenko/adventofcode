from adventofcode.binary_boarding.binary_boarding import *


def test_puzzle_input():
    puzzle_input = read_puzzle_input()
    assert puzzle_input


def test_find_row():
    number_of_rows = 127
    boarding_pass = "FBFBBFFRLR"
    row = find_row(boarding_pass, number_of_rows)
    assert row == 44


def test_find_column():
    number_of_columns = 7
    boarding_pass = "FBFBBFFRLR" # RLR
    column = find_column(boarding_pass, number_of_columns)
    assert column == 5


"""
The last three characters will be either L or R; these specify exactly one of the 
8 columns of seats on the plane (numbered 0 through 7). The same process as above 
proceeds again, this time with only three steps. L means to keep the lower half, 
while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:
Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7. x
L means to take the lower half, keeping columns 4 through 5. 
The final R keeps the upper of the two, column 5.

So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.
"""