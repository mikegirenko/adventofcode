from adventofcode.handy_haversacks.handy_haversacks import read_puzzle_input, INPUT_FILE, \
    bag_colors_which_can_contain_shiny_gold_bag, \
    INPUT_FILE_EXAMPLE, can_contain_shiny_gold_bag_directly, can_contain_shiny_gold_bag_indirectly, \
    count_number_of_bags


def test_puzzle_input():
    print(read_puzzle_input(INPUT_FILE))


def test_bag_colors_which_can_contain_shiny_gold_bag():
    list_of_rules = ["shiny gold bags contain 1 dull lime bag",
                     "drab plum bags contain 3 clear lime bags.",
                     "posh beige bags contain 3 faded silver bags, 5 shiny gold bags."]
    bag_colors = bag_colors_which_can_contain_shiny_gold_bag(list_of_rules)

    assert bag_colors == ["posh beige"]


def test_bag_colors_which_can_contain_shiny_gold_bag_with_puzzle_input():
    list_of_rules = read_puzzle_input(INPUT_FILE)
    bag_colors = bag_colors_which_can_contain_shiny_gold_bag(list_of_rules)
    print(bag_colors)
    assert len(bag_colors) == 7  # there are 7 bag colors which can have shiny_gold_bag


def test_can_contain_shiny_gold_bag_directly():
    rule_true = "bright white bags contain 1 shiny gold bag."
    rule_false = "red bags contain 1 yellow bag."
    assert can_contain_shiny_gold_bag_directly(rule_true)
    assert not can_contain_shiny_gold_bag_directly(rule_false)


def test_can_contain_shiny_gold_bag_indirectly():
    rules = read_puzzle_input(INPUT_FILE_EXAMPLE)
    colors = bag_colors_which_can_contain_shiny_gold_bag(rules)
    assert can_contain_shiny_gold_bag_indirectly(rules, colors) == 4


def test_count_number_of_bags():either of which
    rules = read_puzzle_input(INPUT_FILE_EXAMPLE)
    colors = bag_colors_which_can_contain_shiny_gold_bag(rules)
    direct_bags = can_contain_shiny_gold_bag_directly(rules)
    indirect_bags = can_contain_shiny_gold_bag_indirectly(rules, colors)
    assert count_number_of_bags(direct_bags, indirect_bags) == 1
    # it returns 6
    # this is because can_contain_shiny_gold_bag_indirectly counts incorrectly
