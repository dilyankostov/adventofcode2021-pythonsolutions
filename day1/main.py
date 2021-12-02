# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from unittest import TestCase
from assertpy import assert_that


def count_larger_than_prev(int_list: list) -> int:
    if not int_list:
        return 0

    last_num = int_list[0]
    total = 0
    for num in int_list:
        if num > last_num:
            total += 1
        last_num = num

    return total


def turn_num_txt_to_list(file_name: str) -> list:
    with open(file_name, 'r') as numbers:
        return [int(x) for x in numbers]


def count_three_larger(int_list: list) -> int:
    length = len(int_list)
    if length < 4:
        return 0
    total = 0
    three_sum_prev = int_list[0] + int_list[1] + int_list[2]
    for index, num in enumerate(int_list):
        if index + 2 < length:
            three_sum = num + int_list[index + 1] + int_list[index + 2]
            if three_sum > three_sum_prev:
                total += 1
            three_sum_prev = three_sum

    return total


if __name__ == '__main__':
    # EX1 TEST
    numbers_list = turn_num_txt_to_list("numbers_test.txt")
    result = count_larger_than_prev(numbers_list)

    assert_that(result).is_equal_to(7)

    # EX1 REAL
    numbers_list = turn_num_txt_to_list("numbers_real.txt")
    result = count_larger_than_prev(numbers_list)

    print(f"The first result is {result}")

    # EX2 TEST
    numbers_list = turn_num_txt_to_list("numbers_test.txt")
    result = count_three_larger(numbers_list)

    assert_that(result).is_equal_to(5)

    # EX2 REAL
    numbers_list = turn_num_txt_to_list("numbers_real.txt")
    result = count_three_larger(numbers_list)

    print(f"The second result is {result}")