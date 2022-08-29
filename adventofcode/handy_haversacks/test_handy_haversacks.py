from adventofcode.handy_haversacks.handy_haversacks import read_puzzle_input, INPUT_FILE, \
    does_rule_contain_shiny_gold_bag, count_rules


def test_puzzle_input():
    print(read_puzzle_input(INPUT_FILE))


def test_does_rule_contain_shiny_gold_bagg():
    rule = "bright green bags contain 4 drab silver bags, 5 shiny gold bags."
    assert does_rule_contain_shiny_gold_bag(rule) == rule


def test_count_rules():
    list_of_rules = ["drab plum bags contain 3 clear gold bags.",
                     "posh beige bags contain 3 faded silver bags, 3 dim gold bags, 5 shiny gold bags."]

    assert count_rules(list_of_rules) == 1


def test_count_rules_when_rule_starts_with_shiny_gold():
    list_of_rules = ["shiny gold bags contain 1 dull lime bag",
                     "drab plum bags contain 3 clear gold bags.",
                     "posh beige bags contain 3 faded silver bags, 3 dim gold bags, 5 shiny gold bags."]

    assert count_rules(list_of_rules) == 1

