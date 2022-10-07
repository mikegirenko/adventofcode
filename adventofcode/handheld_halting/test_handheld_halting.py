from adventofcode.handheld_halting.handheld_halting import read_puzzle_input, INPUT_FILE, \
    update_accumulator, read_instruction


def test_read_puzzle_input():
    print(read_puzzle_input(INPUT_FILE))


def test_read_instruction():
    instruction_to_read = "acc +4"
    operation, _, _ = read_instruction(instruction_to_read)
    _, argument_plus_minus, _ = read_instruction(instruction_to_read)
    _, _, argument_number = read_instruction(instruction_to_read)
    assert operation == "acc"
    assert argument_plus_minus == "+"
    assert argument_number == 4


def test_update_accumulator_when_acc_plus():
    instructions_to_read = ["acc +3", "acc +1"]
    assert update_accumulator(instructions_to_read) == 4


def test_update_accumulator_when_acc_minus():
    instruction_to_read = ["acc -3"]
    assert update_accumulator(instruction_to_read) == -3


def test_update_accumulator_when_acc_plus_and_minus():
    instructions_to_read = ["acc +3", "acc -1"]
    assert update_accumulator(instructions_to_read) == 2


def test_update_accumulator_when_nop():
    instruction_to_read = ["nop +0"]
    assert update_accumulator(instruction_to_read) == 0


def test_update_accumulator_when_jmp():
    instructions_to_read = ["jmp +1", "acc +2"]
    assert update_accumulator(instructions_to_read) == 2


def test_program_runs_instruction_for_second_time():
    instructions_to_read = ["acc +1", "acc +4", "jmp -2"]
    acc, instr = update_accumulator(instructions_to_read)
    assert acc == 5
    assert instr == "acc +1"


def test_sample_input():
    puzzle_input = read_puzzle_input(INPUT_FILE)
    acc, instr = update_accumulator(puzzle_input)
    assert acc == 5
    assert instr == "acc +1"
