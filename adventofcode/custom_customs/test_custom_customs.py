from adventofcode.custom_customs.custom_customs import read_puzzle_input, \
    remove_extras_from_answers, count_number_of_questions_answered_yes_within_group, \
    calculate_sum_of_counts, INPUT_FILE


def test_puzzle_input():
    list_of_groups = read_puzzle_input(INPUT_FILE)
    assert list_of_groups


def test_remove_n_from_answers():
    list_with_n = ['abc', 'a\nb\nc', 'ab\nac', 'a\na\na\na', 'b']
    print(remove_extras_from_answers(list_with_n))


def test_number_of_questions_answered_yes_within_group():
    group = "abcab"
    assert count_number_of_questions_answered_yes_within_group(group) == 3


def test_number_of_questions_answered_yes_and_n_within_group():
    group = "ab\ncab"
    assert count_number_of_questions_answered_yes_within_group(group) == 3


def test_sum_of_counts():
    list_of_groups = ['abc', 'abc', 'abac', 'aaaa', 'b']
    assert calculate_sum_of_counts(list_of_groups) == 11
