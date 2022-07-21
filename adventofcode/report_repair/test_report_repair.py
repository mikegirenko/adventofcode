from adventofcode.report_repair.report_repair import *


def test_find_entries():
    expected_numbers = [1721, 299]
    lines = read_report()
    actual_numbers = find_entries(lines)
    assert expected_numbers == actual_numbers


def test_multiply_entries():
    entries = [1721, 299]
    assert multiply_entries(entries) == 514579
