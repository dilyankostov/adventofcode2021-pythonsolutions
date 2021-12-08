# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from assertpy import assert_that
import matplotlib.pyplot as plt
import math


def extract_crabs_from_file(file_name: str) -> list[int]:
    with open(file_name, 'r') as data_file:
        return [int(x) for x in data_file.readline().strip().split(",")]


def part1_find_steps_needed_to_x(crabs_list: list[int], x: int) -> int:
    total_cost = 0
    for crab in crabs_list:
        total_cost += abs(crab - x)
    return total_cost


def part2_find_steps_needed_to_x(crabs_list: list[int], x: int) -> float:
    total_cost = 0
    for crab in crabs_list:
        total_cost += abs(crab - x) * (abs(crab - x) + 1) / 2
    return total_cost


def find_next_inner_points(a, b, factor) -> (float, float):
    diff = (b - a) / factor
    c = a + diff
    d = b - diff
    return c, d


def golden_ratio_search(f, f_input, a: int, b: int, precision) -> int:
    gr = (math.sqrt(5) + 1) / 2
    c, d = find_next_inner_points(a, b, gr)
    while abs(a - b) > precision:
        if f(f_input, round(c)) < f(f_input, round(d)):
            a = d
        else:
            b = c
        c, d = find_next_inner_points(a, b, gr)
    return round(a)


def find_min_y_from_range_int_x(f, f_extra_input, i: int, int_range_around: int):
    min_y = f(f_extra_input, i)
    min_i = i
    for i_loop in range(i - int_range_around, i + int_range_around + 1):
        new_min = f(f_extra_input, i_loop)
        if min_y > new_min:
            min_y = new_min
            min_i = i_loop
    return min_i


def plot_answers_in_range(f, f_extra_input, input_i: int, int_range_around: int):
    y_x_dict = {}
    for i in range(input_i - int_range_around, input_i + int_range_around + 1):
        y_x_dict[i] = f(f_extra_input, i)
    plt.plot(y_x_dict.keys(), y_x_dict.values())
    plt.show()


if __name__ == '__main__':

    # PART1 TEST
    crabs = extract_crabs_from_file("data_test.txt")
    assert_that(part1_find_steps_needed_to_x(crabs, 1)).is_equal_to(41)
    assert_that(part1_find_steps_needed_to_x(crabs, 2)).is_equal_to(37)
    assert_that(part1_find_steps_needed_to_x(crabs, 10)).is_equal_to(71)
    position_answer_rough = golden_ratio_search(part1_find_steps_needed_to_x, crabs, min(crabs), max(crabs), 0.5)
    position_answer = find_min_y_from_range_int_x(part1_find_steps_needed_to_x, crabs, position_answer_rough, 3)
    assert_that(position_answer).is_equal_to(2)
    answer = part1_find_steps_needed_to_x(crabs, position_answer)
    assert_that(answer).is_equal_to(37)

    # PART1 REAL
    crabs = extract_crabs_from_file("data_real.txt")
    position_answer_rough = golden_ratio_search(part1_find_steps_needed_to_x, crabs, min(crabs), max(crabs), 0.5)
    position_answer = find_min_y_from_range_int_x(part1_find_steps_needed_to_x, crabs, position_answer_rough, 3)
    assert_that(position_answer).is_not_equal_to(2)
    answer = part1_find_steps_needed_to_x(crabs, position_answer)
    assert_that(answer).is_not_equal_to(37)
    # plot_answers_in_range(part1_find_steps_needed_to_x, crabs, position_answer, 2000)

    print(answer)

    # PART2 TEST
    crabs = extract_crabs_from_file("data_test.txt")
    assert_that(part2_find_steps_needed_to_x(crabs, 5)).is_equal_to(168)
    assert_that(part2_find_steps_needed_to_x(crabs, 2)).is_equal_to(206)
    position_answer_rough = golden_ratio_search(part2_find_steps_needed_to_x, crabs, min(crabs), max(crabs), 0.5)
    position_answer = find_min_y_from_range_int_x(part2_find_steps_needed_to_x, crabs, position_answer_rough, 3)
    assert_that(position_answer).is_equal_to(5)
    answer = part2_find_steps_needed_to_x(crabs, position_answer)
    assert_that(answer).is_equal_to(168)

    # PART2 REAL
    crabs = extract_crabs_from_file("data_real.txt")
    position_answer_rough = golden_ratio_search(part2_find_steps_needed_to_x, crabs, min(crabs), max(crabs), 0.5)
    position_answer = find_min_y_from_range_int_x(part2_find_steps_needed_to_x, crabs, position_answer_rough, 3)
    assert_that(position_answer).is_not_equal_to(5)
    answer = part2_find_steps_needed_to_x(crabs, position_answer)
    assert_that(answer).is_not_equal_to(168)
    # plot_answers_in_range(part2_find_steps_needed_to_x, crabs, position_answer, 2000)

    print(answer)







