from typing import List

NUMBER_OF_ROWS = 127
NUMBER_OF_COLUMNS = 7


def read_puzzle_input() -> List[str]:
    with open("puzzle_input.txt", "r") as file:
        read_data = file.read()
    list_boarding_passes = read_data.split("\n")

    return list_boarding_passes


def find_row(one_row_from_puzzle, all_rows_on_the_plane) -> int:
    first_seven_characters = one_row_from_puzzle[0:7]
    list_of_all_rows_on_the_plane = [int(x) for x in range(all_rows_on_the_plane + 1)]  # make it a list

    first_range = 0
    if first_seven_characters[0] == "F":  # 0 to 63
        first_range = list_of_all_rows_on_the_plane[0:int(len(list_of_all_rows_on_the_plane) / 2)]
    if first_seven_characters[0] == "B":  # 64 to 127
        first_range = list_of_all_rows_on_the_plane[int(len(list_of_all_rows_on_the_plane) / 2):
                                                    len(list_of_all_rows_on_the_plane) + 1]

    second_range = 0
    if first_seven_characters[1] == "F":  # 0 to 31 -OR- 64 to 95
        second_range = first_range[0:int(len(first_range) / 2)]
    if first_seven_characters[1] == "B":  # 32 to 63 -OR- 96 to 127
        second_range = first_range[int(len(first_range) / 2):len(first_range) + 1]

    third_range = 0
    if first_seven_characters[2] == "F":  # 0 to 15 -OR- 64 to 79 -OR- 96 to 111
        third_range = second_range[0:int(len(second_range) / 2)]
    if first_seven_characters[2] == "B":
        third_range = second_range[int(len(second_range) / 2):len(second_range) + 1]

    fourth_range = 0
    if first_seven_characters[3] == "F":
        fourth_range = third_range[0:int(len(third_range) / 2)]
    if first_seven_characters[3] == "B":
        fourth_range = third_range[int(len(third_range) / 2):len(third_range) + 1]

    fifth_range = 0
    if first_seven_characters[4] == "F":
        fifth_range = fourth_range[0:int(len(fourth_range) / 2)]
    if first_seven_characters[4] == "B":
        fifth_range = fourth_range[int(len(fourth_range) / 2):len(fourth_range) + 1]

    sixth_range = 0
    if first_seven_characters[5] == "F":
        sixth_range = fifth_range[0:int(len(fifth_range) / 2)]
    if first_seven_characters[5] == "B":
        sixth_range = fifth_range[int(len(fifth_range) / 2):len(fifth_range) + 1]

    seventh_range = 0
    if first_seven_characters[6] == "F":
        seventh_range = sixth_range[0:int(len(sixth_range) / 2)]
    if first_seven_characters[6] == "B":
        seventh_range = sixth_range[int(len(sixth_range) / 2):len(sixth_range) + 1]

    row = seventh_range[0]  # make it an int

    return row


def find_column(one_row_from_puzzle, all_columns_in_a_row) -> int:
    last_three_characters = one_row_from_puzzle[-3:]
    list_of_columns = [int(x) for x in range(all_columns_in_a_row + 1)]

    first_column = 0
    if last_three_characters[0] == "R":  # 4 to 7
        first_column = list_of_columns[int(len(list_of_columns) / 2): len(list_of_columns)]
    if last_three_characters[0] == "L":  # 0 to 3
        first_column = list_of_columns[0:int(len(list_of_columns) / 2)]

    second_column = 0
    if last_three_characters[1] == "R":  # 4 to 5
        second_column = first_column[int(len(first_column) / 2): len(first_column)]
    if last_three_characters[1] == "L":  # 6 to 7
        second_column = first_column[0:int(len(first_column) / 2)]

    third_column = 0
    if last_three_characters[2] == "R":
        third_column = second_column[int(len(second_column) / 2): len(second_column)]
    if last_three_characters[2] == "L":
        third_column = second_column[0:int(len(second_column) / 2)]

    column = third_column[0]

    return column


def find_seat_id(row, column) -> int:
    unique_seat_id = (row * 8) + column

    return unique_seat_id


def find_highest_seat_id_on_boarding_pass() -> int:
    all_passes = read_puzzle_input()
    all_ids = []

    for each_pass in all_passes:
        row = find_row(each_pass, NUMBER_OF_ROWS)
        column = find_column(each_pass, NUMBER_OF_COLUMNS)
        seat_id = find_seat_id(row, column)
        all_ids.append(seat_id)
    highest_seat_id_on_boarding_pass = max(all_ids)

    return highest_seat_id_on_boarding_pass


def find_my_seat():
    all_passes = read_puzzle_input()
    all_ids = []
    my_seat = 0

    for each_pass in all_passes:
        row = find_row(each_pass, NUMBER_OF_ROWS)
        column = find_column(each_pass, NUMBER_OF_COLUMNS)
        seat_id = find_seat_id(row, column)
        all_ids.append(seat_id)  # create list of all id's
    lowest_id = min(all_ids) # 11
    highest_id = max(all_ids) # 850
    missing_ids = list(set(range(max(all_ids) + 1)) - set(all_ids))  # found it online and it works, using set
    for missing_id in missing_ids:
        if lowest_id < missing_id < highest_id:  # my seat should be above lowest if and below highest
            my_seat = missing_id

    return my_seat
