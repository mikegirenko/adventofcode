from typing import List

INPUT_FILE = "puzzle_input.txt"
INPUT_FILE_EXAMPLE = "puzzle_input_example.txt"


def read_puzzle_input(puzzle_input) -> List[str]:
    with open(puzzle_input, "r") as file:
        read_data = file.read()
    list_of_groups = read_data.split("\n")

    return list_of_groups


# determine bag colors which can contain shiny gold,
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


def can_contain_shiny_gold_bag_directly(list_of_rules) -> bool:
    rows_counter = 0
    for rule in list_of_rules:
        if not rule.startswith("shiny gold") and "shiny gold bag" in rule:
            rows_counter += 1

    return rows_counter


def can_contain_shiny_gold_bag_indirectly(list_of_rules, colors):
    rows_counter = 0
    for rule in list_of_rules:
        already_counted_color = True
        for color in colors:
            if color in rule and "shiny gold bag" not in rule:
                if not already_counted_color:
                    continue
                rows_counter += 1
                already_counted_color = False

    return rows_counter


def count_number_of_bags(direct_bags, indirect_bags):
    return direct_bags + indirect_bags


if __name__ == "__main__":
    list_of_rules_from_input = read_puzzle_input(INPUT_FILE)
    bag_colors = bag_colors_which_can_contain_shiny_gold_bag(list_of_rules_from_input)
    direct_bags = can_contain_shiny_gold_bag_directly(list_of_rules_from_input)
    indirect_bags = can_contain_shiny_gold_bag_indirectly(list_of_rules_from_input, bag_colors)
    result = count_number_of_bags(direct_bags, indirect_bags)
    print("How many bag colors can eventually contain at least one shiny gold bag?", result)
    # 27
    # That's not the right answer.
