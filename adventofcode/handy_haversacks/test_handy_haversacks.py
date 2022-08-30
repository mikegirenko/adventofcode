from adventofcode.handy_haversacks.handy_haversacks import read_puzzle_input, INPUT_FILE, \
    count_rows_on_the_list_which_have_one_bag_color, bag_colors_which_can_contain_shiny_gold_bag


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


def test_count_rules():
    list_of_rules = ["5 posh beige bags", "1 dotted orange bags", "5 posh beige bags"]
    bag_colors = ["posh beige", "dotted orange"]
    rows_count = count_rows_on_the_list_which_have_one_bag_color(list_of_rules, bag_colors)
    assert rows_count == 3
