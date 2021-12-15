# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from assertpy import assert_that


def count_smaller_than_nth(int_list: list, n: int) -> int:
    """
    counts the number numbers that are smaller than the number that is n ahead
    """
    if len(int_list) <= n:
        return 0
    total = 0
    for i in range(0, len(int_list) - n):
        if int_list[i + n] > int_list[i]:
            total += 1
    return total


def turn_num_txt_to_list(file_name: str) -> list:
    with open(file_name, 'r') as numbers:
        return [int(x) for x in numbers]


if __name__ == '__main__':
    # EX1 TEST
    numbers_list = turn_num_txt_to_list("data_test.txt")
    result = count_smaller_than_nth(numbers_list, 1)

    assert_that(result).is_equal_to(7)

    # EX1 REAL
    numbers_list = turn_num_txt_to_list("data_real.txt")
    result = count_smaller_than_nth(numbers_list, 1)

    print(f"The first result is {result}")

    # EX2 TEST
    # If you think about it, a three-measurement sliding window has the elements A+B+C,
    # while the next window is B+C+D so the difference is A+B+C-B-C-D = A-D
    # so we don't need to sum anything, just check if A is smaller than D
    numbers_list = turn_num_txt_to_list("data_test.txt")
    result = count_smaller_than_nth(numbers_list, 3)

    assert_that(result).is_equal_to(5)

    # EX2 REAL
    numbers_list = turn_num_txt_to_list("data_real.txt")
    result = count_smaller_than_nth(numbers_list, 3)

    print(f"The second result is {result}")