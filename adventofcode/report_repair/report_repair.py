# Completing https://adventofcode.com/2020/day/1
from typing import List


def read_report() -> List[str]:
    with open("report.txt", "r") as file:
        read_data = file.read()
    file_lines = read_data.split("\n")

    return file_lines


def find_two_entries(input_lines: List[str]) -> List[int]:
    report = input_lines
    i = 0
    two_entries = []
    while i < len(report):
        entry_one = int(report[i])  # first element
        remaining_list = report[i + 1 :]  # remaining list
        for entry_two in remaining_list:
            entry_two_int = int(entry_two)
            if entry_one + entry_two_int == 2020:
                two_entries.append(entry_one)
                two_entries.append(entry_two_int)
        i = i + 1

    return two_entries


def find_three_entries(input_lines: List[str]) -> List[int]:
    i = 0
    three_entries = []
    for i in range(0, len(input_lines) - 2):
        for j in range(i + 1, len(input_lines) - 1):
            for k in range(j + 1, len(input_lines)):
                if (
                    int(input_lines[i]) + int(input_lines[j]) + int(input_lines[k])
                    == 2020
                ):
                    three_entries.append(int(input_lines[i]))
                    three_entries.append(int(input_lines[j]))
                    three_entries.append(int(input_lines[k]))
    return three_entries


def multiply_two_entries(input_entries: List[int]) -> int:
    entries = find_two_entries(input_entries)

    return entries[0] * entries[1]


def multiply_three_entries(input_entries: List[int]) -> int:
    entries = find_three_entries(input_entries)

    return entries[0] * entries[1] * entries[2]


if __name__ == "__main__":
    report_entries = read_report()

    entries_found = find_two_entries(report_entries)
    result = multiply_two_entries(entries_found)
    print("Two entries Answer is", result)

    entries_found = find_three_entries(report_entries)
    result = multiply_three_entries(entries_found)
    print("Three entries Answer is", result)
