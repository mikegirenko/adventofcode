from typing import List

# Requirements
# find row


def read_puzzle_input() -> List[str]:
    with open("puzzle_input.txt", "r") as file:
        read_data = file.read()
    list_of_passwords = read_data.split("\n")

    return list_of_passwords


def find_row(row_from_input, all_rows) -> int:
    whole_row = row_from_input
    whole_range_of_rows = all_rows
    first_seven_characters = whole_row[0:7]
    list_of_rows = [int(x) for x in range(whole_range_of_rows + 1)] # make it a list

    first_range = 0
    if first_seven_characters[0] == "F": # 0 to 63
        first_range = list_of_rows[0:int(len(list_of_rows) / 2)]
    if first_seven_characters[0] == "B": # 64 to 127
        first_range = list_of_rows[int(len(list_of_rows) / 2):len(list_of_rows) + 1]

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

    row = seventh_range[0] # make it an int

    return row


def find_column(row_from_input, all_columns):
    whole_row = row_from_input
    whole_range_of_columns = all_columns
    last_three_characters = whole_row[-3:]
    list_of_columns = [int(x) for x in range(whole_range_of_columns + 1)]

    first_column = 0
    if last_three_characters[0] == "R": # 4 to 7
        first_column = list_of_columns[int(len(list_of_columns) / 2): len(list_of_columns)]
    if last_three_characters[0] == "L": # 0 to 3
        first_column = list_of_columns[0:int(len(list_of_columns) / 2)]


    # second_column = 0
    if last_three_characters[1] == "R": # 4 to 5
        second_column = first_column[int(len(first_column) / 2): len(first_column)]
    if last_three_characters[1] == "L": # 6 to 7
        second_column = first_column[0:int(len(first_column) / 2)]

    # third_column = 0
    if last_three_characters[2] == "R":
        third_column = second_column[int(len(second_column) / 2): len(second_column)]
    if last_three_characters[2] == "L":
        third_column = second_column[0:int(len(second_column) / 2)]

    column = third_column[0]

    return column
