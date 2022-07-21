from adventofcode.passport_processing.passport_processing import *


def test_file_reading():
    assert len(read_file()) == 279


def test_remove_n_from_password():
    this_file = read_file()
    clean_list_of_passwords = remove_n_from_password(this_file)
    for password in clean_list_of_passwords:
        for char in password:
            assert char != "\n"


def test_has_all_required_fields_in_a_passport():
    this_file = "byr iyr eyr hgt hcl ecl pid cid"
    assert detect_required_fields_in_a_passport(this_file)


def test_does_not_have_all_required_fields_in_a_passport():
    this_file = "mmm iyr eyr hgt hcl ecl pid cid"
    assert not detect_required_fields_in_a_passport(this_file)


def test_cid_is_not_required_field():
    this_file = "byr iyr eyr hgt hcl ecl pid"
    assert detect_required_fields_in_a_passport(this_file)


def test_detect_which_passports_have_all_required_fields():
    this_file = read_file()
    clean_list_of_passwords = remove_n_from_password(this_file)
    assert count_valid__passports_(clean_list_of_passwords) == 213
    # Your puzzle answer was 213.
