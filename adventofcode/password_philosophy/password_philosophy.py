# Completing https://adventofcode.com/2020/day/2

list_of_passwords = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]


def get_policy(password_index):
    return list_of_passwords[password_index][0:5]


def policy_details(password_index):
    policy = get_policy(password_index)
    return policy[0], policy[2], policy[4]


def just_password(password_index):
    just_this_password = list_of_passwords[password_index][6:]
    return just_this_password


def find_valid_password():
    i = 0
    valid_passwords = []
    while i < len(list_of_passwords):
        letters_count = 0
        this_policy_details = policy_details(i)
        lowest_number_of_times, _, _ = this_policy_details
        _, highest_number_of_times, _ = this_policy_details
        _, _, letter = this_policy_details
        password_only = just_password(i)
        i += 1
        for item in password_only:
            if item == letter:
                letters_count += 1
        if int(lowest_number_of_times) <= letters_count <= int(highest_number_of_times):
            valid_passwords.append(password_only)
    return valid_passwords
