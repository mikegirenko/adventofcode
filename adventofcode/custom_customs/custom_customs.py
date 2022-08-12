from typing import List
import re

INPUT_FILE = "puzzle_input.txt"


def read_puzzle_input(puzzle_input) -> List[str]:
    with open(puzzle_input, "r") as file:
        read_data = file.read()
    list_of_groups = read_data.split("\n\n")

    return list_of_groups


# this is to remove \n and then "" from each answer which has a new line
def remove_extras_from_answers(list_of_answers) -> List[str]:
    clean_list_of_answers = []
    for i in list_of_answers:
        i = i.replace("\n", "")
        if i != "":
            clean_list_of_answers.append(i)

    return clean_list_of_answers


def count_number_of_questions_answered_yes_within_group(group) -> int:
    group_without_n = remove_extras_from_answers(group)

    # using set which assures unique character because "each question counts at most once"
    return len(set(group_without_n))


def calculate_sum_of_counts(list_of_groups) -> int:
    sum_of_counts = 0
    for group in list_of_groups:
        count = count_number_of_questions_answered_yes_within_group(group)
        sum_of_counts = sum_of_counts + count

    return sum_of_counts


# identify the questions to which everyone answered "yes"
def count_questions_in_a_group_to_which_everyone_answered_yes(group):
    questions_count = 0
    common_char = []
    i = 0
    if "\n" not in group:
        questions_count = len(set(group))
    if "\n" in group:
        list_of_groups = group.split("\n")
        while i < len(list_of_groups):
            for char in list_of_groups[-1]:
                if re.search(char, list_of_groups[i]):
                    if char not in common_char:
                        common_char.append(char)
            i += 1
        questions_count = len(common_char)
    return questions_count


def calculate_sum_of_yes_answers(list_of_groups) -> int:
    sum_of_yes = 0
    for group in list_of_groups:
        count = count_questions_in_a_group_to_which_everyone_answered_yes(group)
        sum_of_yes = sum_of_yes + count

    return sum_of_yes


if __name__ == "__main__":
    groups_of_answers = read_puzzle_input(INPUT_FILE)
    print("Sum of counts is", calculate_sum_of_counts(groups_of_answers))
    # Sum of counts is 6630
    # That's the right answer! You are one gold star closer to saving your vacation.

    print("Sum of all yes for all groups", calculate_sum_of_yes_answers(groups_of_answers))
    # Sum of all yes for all groups 4521
    # That's not the right answer.
