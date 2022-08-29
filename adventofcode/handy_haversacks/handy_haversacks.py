from typing import List

INPUT_FILE = "puzzle_input.txt"


def read_puzzle_input(puzzle_input) -> List[str]:
    with open(puzzle_input, "r") as file:
        read_data = file.read()
    list_of_groups = read_data.split("\n")

    return list_of_groups


def does_rule_contain_shiny_gold_bag(rule) -> List:
    if "shiny gold bag" in rule:
        return rule


def count_rules(list_of_rules) -> int:
    counter = 0
    for rule in list_of_rules:
        if rule.startswith("shiny gold"):
            continue
        if does_rule_contain_shiny_gold_bag(rule):
            counter += 1

    return counter


if __name__ == "__main__":
    list_of_rules_from_input = read_puzzle_input(INPUT_FILE)
    bag_colors = count_rules(list_of_rules_from_input)
    print("How many bag colors can eventually contain at least one shiny gold bag?", bag_colors)
