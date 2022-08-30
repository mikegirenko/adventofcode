from typing import List
import re

INPUT_FILE = "puzzle_input.txt"


def read_puzzle_input(puzzle_input) -> List[str]:
    with open(puzzle_input, "r") as file:
        read_data = file.read()
    list_of_groups = read_data.split("\n")

    return list_of_groups

# this will determine bag colors which can contain shiny gold
# except a rule which starts with "shiny gold"
def bag_colors_which_can_contain_shiny_gold_bag(list_of_rules) -> List:
    rules = []
    bag_colors = []
    for rule in list_of_rules:
        if rule.startswith("shiny gold"):
            continue
        if "shiny gold bag" in rule:
            rules.append(rule)

    for rule in rules:
        bag_color = rule.split(" ")
        bag_color_combined = bag_color[0] + " " + bag_color[1]
        bag_colors.append(bag_color_combined)

    return bag_colors
# ['posh beige', 'dotted orange', 'bright green', 'faded violet', 'dark olive',
# 'shiny orange', 'dark tomato']


# find each row which has at least one bag color which can contain "shiny gold bag"
def count_rows_on_the_list_which_have_one_bag_color(list_of_rules, bag_colors) -> int:
    rows_counter = 0
    for rule in list_of_rules:
        for bag_color in bag_colors:
            if bag_color in rule:
                rows_counter += 1

    return rows_counter


if __name__ == "__main__":
    list_of_rules_from_input = read_puzzle_input(INPUT_FILE)
    bag_colors = bag_colors_which_can_contain_shiny_gold_bag(list_of_rules_from_input)
    result = count_rows_on_the_list_which_have_one_bag_color(list_of_rules_from_input, bag_colors)
    print("How many bag colors can eventually contain at least one shiny gold bag?", result)
    # 27
    # That's not the right answer.