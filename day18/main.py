# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from assertpy import assert_that
from itertools import permutations
from math import floor, ceil


def extract_data_from_file(file_name: str) -> list[list[str, int]]:
    nums = []
    with open(file_name, 'r') as data_file:
        for line in data_file:
            data = [i for i in line.strip() if i != ',']
            nums.append([int(i) if i.isdigit() else i for i in data])
        return nums


def from_str(string: str) -> list[str, int]:
    return [int(i) if i.isdigit() else i for i in string.strip() if i != ',']


def calc_sum(num: list[str, int]) -> int:
    i = 0
    while True:
        if len(num) == 1:
            return int(num[0])
        if num[i] == ']':
            new_num = 3 * num[i-2] + 2 * num[i-1]
            del num[i-3:i+1]
            num.insert(i-3, new_num)
            i = i - 3
        i += 1


def incr_next(num: list[str], i: int, direction: str = "right"):
    if direction == "right":
        rng = range(i + 1, len(num))
    else:
        rng = range(i - 1, -1, -1)
    for z in rng:
        if isinstance(num[z], int):
            num[z] = num[z] + num[i]
            break


def search_n_explode(num) -> bool:
    brackets = 0
    for i in range(len(num)):
        if num[i] == "[":
            brackets += 1
        elif num[i] == "]":
            brackets -= 1
        elif brackets > 4:
            incr_next(num, i, "left")
            incr_next(num, i + 1)
            del num[i - 1:i + 3]
            num.insert(i - 1, 0)
            return True
    return False


def seek_n_split(num) -> bool:
    for i in range(len(num)):
        if isinstance(num[i], int):
            if num[i] > 9:
                num.insert(i + 1, '[')
                num.insert(i + 2, floor(num[i] / 2))
                num.insert(i + 3, ceil(num[i] / 2))
                num.insert(i + 4, ']')
                del num[i]
                return True
    return False


def do_math(num: list[str, int]) -> list[str, int]:
    while True:
        is_explosion = search_n_explode(num)
        if is_explosion:
            continue
        is_split = seek_n_split(num)
        if not is_split:
            break
    return num


def calc_all_nums(list_of_nums: list[list[str, int]]):
    if len(list_of_nums) == 1:
        return calc_sum(do_math(list_of_nums[0]))
    result = list_of_nums[0]
    for i in range(1, len(list_of_nums)):
        result = do_math(['[', *result, *list_of_nums[i], ']'])
    return calc_sum(result)


def calc_largest_diff(list_of_nums: list[list[str, int]]):
    max_diff = 0
    for num1, num2 in permutations(list_of_nums, 2):
        max_diff = max(max_diff, calc_sum(do_math(['[', *num1, *num2, ']'])))
    return max_diff


if __name__ == '__main__':
    # PART1 TEST
    crab_nums = extract_data_from_file("data_test1.txt")
    assert_that(calc_sum(from_str("[[1,2],[[3,4],5]]"))).is_equal_to(143)
    assert_that(calc_sum(from_str("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"))).is_equal_to(1384)
    assert_that(calc_sum(from_str("[[[[1,1],[2,2]],[3,3]],[4,4]]"))).is_equal_to(445)
    assert_that(calc_sum(from_str("[[[[3,0],[5,3]],[4,4]],[5,5]]"))).is_equal_to(791)
    assert_that(calc_sum(from_str("[[[[5,0],[7,4]],[5,5]],[6,6]]"))).is_equal_to(1137)
    assert_that(calc_sum(from_str("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"))).is_equal_to(3488)
    answer = do_math(from_str("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"))
    assert_that(calc_sum(answer)).is_equal_to(calc_sum(from_str("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")))
    answer = calc_all_nums(crab_nums)
    assert_that(answer).is_equal_to(calc_sum(from_str("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")))
    crab_nums_2 = extract_data_from_file("data_test2.txt")
    answer_p1 = calc_all_nums(crab_nums_2)
    assert_that(answer_p1).is_equal_to(4140)
    answer_p2 = calc_largest_diff(crab_nums_2)
    assert_that(answer_p2).is_equal_to(3993)

    # PART1 REAL
    crab_nums_real = extract_data_from_file("data_real.txt")
    answer_p1 = calc_all_nums(crab_nums_real)
    answer_p2 = calc_largest_diff(crab_nums_real)
    print(answer_p1)
    assert_that(answer_p2).is_less_than(4848)
    print(answer_p2)
