from adventofcode.report_repair.report_repair import *


def test_find_two_entries():
    expected_numbers = [81, 1939]
    lines = [81, 1939, 1883, 1698]
    actual_numbers = find_two_entries(lines)
    assert expected_numbers == actual_numbers


def test_multiply_two_entries():
    entries = [1721, 299]
    assert multiply_two_entries(entries) == 514579


def test_find_three_entries():
    input_lines = [4, 80, 0, 1939, 1]
    expected_numbers = [80, 1939, 1]
    actual_numbers = find_three_entries(input_lines)
    assert expected_numbers == actual_numbers


def test_multiply_three_entries():
    entries = [4, 80, 0, 1939, 1]
    assert multiply_three_entries(entries) == 155120
