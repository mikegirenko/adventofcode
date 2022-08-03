# Completing https://adventofcode.com/2020/day/2
from typing import List


def read_puzzle_input() -> List[str]:
    with open("puzzle_input.txt", "r") as file:
        read_data = file.read()
    file_lines = read_data.split("\n")

    return file_lines


def get_policy(one_password):
    return one_password[0:5]


def get_policy_details(one_password):
    return one_password[0], one_password[2], one_password[4]


def get_password_only(one_password):
    return one_password[6:]


def find_valid_password(list_of_passwords):
    valid_passwords = []
    for password in list_of_passwords:
        letters_count = 0
        this_policy_details = get_policy_details(password)
        lowest_number_of_times, _, _ = this_policy_details
        _, highest_number_of_times, _ = this_policy_details
        _, _, letter = this_policy_details
        password_only = get_password_only(password)
        for item in password_only:
            if item == letter:
                letters_count += 1
        if int(lowest_number_of_times) <= letters_count <= int(highest_number_of_times):
            valid_passwords.append(password_only)

    return valid_passwords


def count_valid_passwords():
    list_of_passwords = read_puzzle_input()
    print("There are", len(find_valid_password(list_of_passwords)), "valid passwords")


if __name__ == "__main__":
    count_valid_passwords()
