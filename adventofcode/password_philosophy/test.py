from adventofcode.password_philosophy.password_philosophy import *

expected_list_of_passwords = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]


def test_get_policy():
    assert get_policy(0) == expected_list_of_passwords[0][0:5]


def test_policy_details():
    password_index = 0
    policy_deets = policy_details(password_index)
    lowest_number_of_times, _, _ = policy_deets
    assert int(lowest_number_of_times) == 1
    _, highest_number_of_times, _ = policy_deets
    assert int(highest_number_of_times) == 3
    _, _, letter = policy_deets
    assert letter == "a"


def test_just_password():
    password_index = 0
    assert just_password(password_index) == expected_list_of_passwords[password_index][6:]


def test_find_valid_password():
    assert find_valid_password() == [' abcde', ' ccccccccc']
