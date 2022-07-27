from typing import List

# Requirements
# find row


def read_puzzle_input() -> List[str]:
    with open("puzzle_input.txt", "r") as file:
        read_data = file.read()
    list_of_passwords = read_data.split("\n")

    return list_of_passwords


def find_row(row_from_input):
    whole_range_of_rows = 127
    low_range = 0
    high_range = 0
    whole_row = row_from_input
    first_seven_characters = whole_row[0:7]
    list_if_rows = [int(x) for x in range(whole_range_of_rows + 1)]
    first_range = 0
    if first_seven_characters[0] == "F": # 0 to 63
        first_range = list_if_rows[0:int(len(list_if_rows) / 2)]
    if first_seven_characters[0] == "B": # 64 to 127
        first_range = list_if_rows[int(len(list_if_rows) / 2):len(list_if_rows) + 1]

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

    return seventh_range


    # first_range = slice(len(list_if_rows) // 2, len(list_if_rows)) # list_if_rows[64:128]

    # s = "string"
    # a = len(s)
    # s1 = slice(0, len(s) // 2)
    # s2 = slice(len(s) // 2, len(s))
    # print(s[s1], s[s2])

    # if first_seven_characters[0] == "F": # then 0 to 63
    #     second_range = list_if_rows[0:64]
    # if first_seven_characters[0] == "B": # then 64 to 127
    #     first_range = list_if_rows[64:128]

    #
    # if first_seven_characters[0] == "F": # then 0 to 63
    #     low_range = low_range
    #     high_range = int(whole_range_of_rows / 2)
    #
    # if first_seven_characters[0] == "B": # then 64 to 127
    #     low_range = whole_range_of_rows - int(whole_range_of_rows / 2)
    #     high_range = whole_range_of_rows
    #
    # if first_seven_characters[1] == "F": # 0 to 31
    #     low_range = int(low_range / 2)
    #     high_range = int(high_range / 2)
    # if first_seven_characters[1] == "B": # 32 tp 63
    #     low_range = high_range - int(high_range / 2)
    #     high_range = high_range
    #
    # if first_seven_characters[2] == "F":  # 0 to 15
    #     low_range = int(low_range / 2)
    #     high_range = int(high_range / 2)
    # if first_seven_characters[2] == "B":
    #     low_range = high_range - int(high_range / 2)
    #     high_range = high_range

    # return low_range, high_range


