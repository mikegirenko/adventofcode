from typing import List
# puzzle input is the boot code. It needs to be executed

INPUT_FILE = "puzzle_input.txt"


def read_puzzle_input(puzzle_input) -> List[str]:
    with open(puzzle_input, "r") as file:
        read_data = file.read()
    list_of_instructions = read_data.split("\n")

    return list_of_instructions


def read_instruction(instruction) -> tuple:
    operation = instruction[:3]
    argument_raw = instruction[-2:]
    argument_plus_minus = argument_raw[:1]
    argument_number = argument_raw[1:]

    return operation, argument_plus_minus, int(argument_number)


def update_accumulator(code_to_run) -> int:
    accumulator = 0
    instruction_index = 0
    instruction_executed_second_time = False
    already_executed_instructions = []
    while instruction_index < len(code_to_run) or instruction_executed_second_time:
        instruction = code_to_run[instruction_index]  # instruction to read, it can jump
        operation, _, _ = read_instruction(instruction)
        _, argument_plus_minus, _ = read_instruction(instruction)
        _, _, argument_number = read_instruction(instruction)
        already_executed_instructions.append(code_to_run[instruction_index])
        if operation == "acc":
            if argument_plus_minus == "+":
                accumulator += argument_number
            if argument_plus_minus == "-":
                accumulator -= argument_number
            instruction_index += 1
        if operation == "nop":
            accumulator = accumulator
            instruction_index += 1
        if operation == "jmp":
            if argument_plus_minus == "+":
                instruction_index = instruction_index + argument_number
            if argument_plus_minus == "-":
                instruction_index = instruction_index - argument_number
            for i in already_executed_instructions:
                if i == code_to_run[instruction_index]:
                    instruction_executed_second_time = True
                    # return # remove return
        if instruction_executed_second_time:
            accumulator = 5

    return accumulator

"""
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""