# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from unittest import TestCase
from assertpy import assert_that


def get_directions_from_file(file_name: str) -> list[tuple[str, int]]:
    return_instr = []
    with open(file_name, 'r') as f:
        for instruction in f:
            direction, depth = instruction.split(" ")
            return_instr.append((direction.lower(), int(depth.strip())))

    return return_instr


def get_distance(instuctions, which_part: str = "part1"):
    x, y, y1 = 0, 0, 0
    for direction, delta in instuctions:
        if direction == 'forward':
            x += delta
            y1 += y * delta
        elif direction == 'up':
            y -= delta
        elif direction == 'down':
            y += delta

    if "1" in which_part:
        return x * y
    else:
        return x * y1


if __name__ == '__main__':
    # PART1 TEST
    instructions = get_directions_from_file("data_test.txt")
    result = get_distance(instructions, "part1")

    assert_that(result).is_equal_to(150)

    # PART1 REAL
    instructions = get_directions_from_file("data_real.txt")
    result = get_distance(instructions, "part1")

    print(f"The result of part 1 is {result}")

    # PART2 TEST
    instructions = get_directions_from_file("data_test.txt")
    result = get_distance(instructions, "part2")
    print(f"The result of part 2 TEST data is {result}")
    assert_that(result).is_equal_to(900)

    instructions = get_directions_from_file("data_real.txt")
    result = get_distance(instructions, "part2")
    print(f"The result of part 2 REAL data is {result}")
    print(result)
