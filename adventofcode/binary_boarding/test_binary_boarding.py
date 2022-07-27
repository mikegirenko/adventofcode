from adventofcode.binary_boarding.binary_boarding import *


def test_puzzle_input():
    puzzle_input = read_puzzle_input()

    assert len(puzzle_input) == 839


def test_find_row():
    boarding_pass = "FBFBBFFRLR" # FBFBBFF is first seven characters
    row = find_row(boarding_pass, NUMBER_OF_ROWS)

    assert row == 44


def test_find_column():
    boarding_pass = "FBFBBFFRLR" # RLR is last three characters
    column = find_column(boarding_pass, NUMBER_OF_COLUMNS)

    assert column == 5


def test_find_seat_id():
    row = 44
    column = 5
    unique_seat_id = find_seat_id(row, column)

    assert unique_seat_id == 357


def test_find_seat_id_acceptance_test_one():
    boarding_pass = "BFFFBBFRRR"
    row = find_row(boarding_pass, NUMBER_OF_ROWS)
    column = find_column(boarding_pass, NUMBER_OF_COLUMNS)
    unique_seat_id = find_seat_id(row, column)

    assert unique_seat_id == 567


def test_find_seat_id_acceptance_test_two():
    boarding_pass = "FFFBBBFRRR"
    row = find_row(boarding_pass, NUMBER_OF_ROWS)
    column = find_column(boarding_pass, NUMBER_OF_COLUMNS)
    unique_seat_id = find_seat_id(row, column)

    assert unique_seat_id == 119


def test_find_seat_id_acceptance_test_three():
    boarding_pass = "BBFFBBFRLL"
    row = find_row(boarding_pass, NUMBER_OF_ROWS)
    column = find_column(boarding_pass, NUMBER_OF_COLUMNS)
    unique_seat_id = find_seat_id(row, column)

    assert unique_seat_id == 820


def test_find_highest_seat_id_on_boarding_pass():
    highest_seat_id_on_boarding_pass = find_highest_seat_id_on_boarding_pass()

    assert highest_seat_id_on_boarding_pass == 850


def test_find_my_seat():
    my_seat = find_my_seat()

    assert my_seat == 599
