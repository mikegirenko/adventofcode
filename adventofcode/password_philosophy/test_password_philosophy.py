from adventofcode.password_philosophy.password_philosophy import *


def test_read_puzzle_input():
    print(read_puzzle_input())


def test_get_policy():
    password = "1-3 a: abcde"
    assert get_policy(password) == password[0:5]


def test_policy_details():
    password = "1-3 a: abcde"
    policy_deets = get_policy_details(password)
    lowest_number_of_times, _, _ = policy_deets
    assert int(lowest_number_of_times) == 1
    _, highest_number_of_times, _ = policy_deets
    assert int(highest_number_of_times) == 3
    _, _, letter = policy_deets
    assert letter == "a"


def test_password_only():
    password = "1-3 a: abcde"
    assert get_password_only(password) == password[6:]


def test_find_valid_password():
    list_of_passwords = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    assert len(find_valid_password(list_of_passwords)) == 2
