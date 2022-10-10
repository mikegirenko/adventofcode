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
    argument_split = instruction.split(" ")
    argument = argument_split[1]
    argument_plus_minus = argument[0]
    argument_number = argument[1:]

    return operation, argument_plus_minus, int(argument_number)


def run_code(code_to_run) -> tuple:
    accumulator = 0
    accumulator_before_instruction_executed_second_time = 0
    instruction_index = 0
    instruction_executed_second_time = False
    instruction_being_executed_second_time = ""
    already_executed_instructions = []
    already_jumped = False
    while instruction_index < len(code_to_run) or instruction_executed_second_time:
        instruction = code_to_run[instruction_index]
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
                if i == code_to_run[instruction_index] and already_jumped:
                    instruction_executed_second_time = True
                    instruction_being_executed_second_time = code_to_run[instruction_index]
                    accumulator_before_instruction_executed_second_time = accumulator
            already_jumped = True
        if instruction_executed_second_time:
            return accumulator_before_instruction_executed_second_time, instruction_being_executed_second_time

    return accumulator


if __name__ == "__main__":
    puzzle_input = read_puzzle_input(INPUT_FILE)
    accumulator_value, instruction_executed_second_time = run_code(puzzle_input)
    print("Accumulator value is", accumulator_value, "and instruction executed for the second time is", instruction_executed_second_time)
