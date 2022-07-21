from typing import List

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]


def read_file() -> List[str]:
    with open("batch_file.txt", "r") as file:
        read_data = file.read()
    list_of_passwords = read_data.split("\n\n") # this is how I am splitting file on blank line

    return list_of_passwords


# this is to remove \n from each password which has a new line
def remove_n_from_password(list_of_passwords) -> List[str]:
    clean_list_of_passwords = []
    for i in list_of_passwords:
        i = i.replace("\n", " ")
        clean_list_of_passwords.append(i)

    return clean_list_of_passwords


def detect_required_fields_in_a_passport(one_passport) -> bool:
    has_required_fields = False
    valid_fields_counter = 0
    password_to_list = one_passport.split(" ")
    for field in required_fields:
        for item in password_to_list:
            if field in item and field != "cid":
                valid_fields_counter += 1
    if valid_fields_counter == 7:  # not counting "cid" as required
        has_required_fields = True

    return has_required_fields


def count_valid__passports_(file_with_passports) -> int:
    number_of_valid_passports = 0
    for passport in file_with_passports:
        if detect_required_fields_in_a_passport(passport):
            number_of_valid_passports += 1

    return number_of_valid_passports
