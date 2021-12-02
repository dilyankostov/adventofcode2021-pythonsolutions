# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from unittest import TestCase
from assertpy import assert_that
from typing import Dict
import math


def turn_directions_file_to_dict(file_name: str) -> Dict[str, int]:
    return_dict = {}
    with open(file_name, 'r') as instructions:
        for instruction in instructions:
            direction, depth = instruction.split(" ")
            direction, depth = direction.lower(), int(depth)
            return_dict[direction] = return_dict.get(direction, 0) + depth

    return return_dict


def check_allowed_data(dict_to_check: Dict[str, int]) -> bool:
    for key in dict_to_check:
        if key not in ['down', 'forward', 'up']:
            return False
    return True


def calc_2dim_dir_part1(directions_dict: Dict[str, int]) -> Dict[str, int]:
    coord_dict = {}
    for key, value in directions_dict.items():
        if key == 'forward':
            coord_dict['horizontal'] = coord_dict.get('horizontal', 0) + value
        elif key == 'down':
            coord_dict['depth'] = coord_dict.get('depth', 0) + value
        elif key == 'up':
            coord_dict['depth'] = coord_dict.get('depth', 0) - value
        else:
            raise KeyError(f'Wrong Key, key "{key}" does not exist')
    return coord_dict


def calc_2dim_dir_part2(coordinates: Dict[str, int], directions_dict: Dict[str, int]) -> Dict[str, int]:
    for key, value in directions_dict.items():
        if key == 'forward':
            coordinates['horizontal'] = coordinates.get('horizontal', 0) + value
            coordinates['depth'] = coordinates.get('depth', 0) + value * coordinates.get('aim', 0)
        elif key == 'down':
            coordinates['aim'] = coordinates.get('aim', 0) + value
        elif key == 'up':
            coordinates['aim'] = coordinates.get('aim', 0) - value
        else:
            raise KeyError(f'Wrong Key, key "{key}" does not exist')
    return coordinates


def get_coords_from_txt_file(file_name: str) -> int:
    with open(file_name, 'r') as instructions:
        current_coords = {}
        for instruction in instructions:
            direction, depth = instruction.split(" ")
            current_directions: dict = {direction.lower(): int(depth)}
            assert_that(check_allowed_data(current_directions)).is_equal_to(True)

            current_coords = calc_2dim_dir_part2(current_coords, current_directions)
    return current_coords['horizontal'] * current_coords['depth']


if __name__ == '__main__':
    # PART1 TEST
    numbers_list = turn_directions_file_to_dict("data_test.txt")
    assert_that(check_allowed_data(numbers_list)).is_equal_to(True)
    coord_2d = calc_2dim_dir_part1(numbers_list)
    result = math.prod(coord_2d.values())

    assert_that(result).is_equal_to(150)

    # PART1 REAL
    numbers_list = turn_directions_file_to_dict("data_real.txt")
    assert_that(check_allowed_data(numbers_list)).is_equal_to(True)
    coord_2d = calc_2dim_dir_part1(numbers_list)
    result = math.prod(coord_2d.values())

    # print(f"The result of part 1 is {result}")
    # print(result)

    # PART2 TEST
    result = get_coords_from_txt_file('data_test.txt')
    print(f"The result of part 2 TEST data is {result}")
    assert_that(result).is_equal_to(900)

    result = get_coords_from_txt_file('data_real.txt')
    print(f"The result of part 2 REAL data is {result}")
    print(result)


