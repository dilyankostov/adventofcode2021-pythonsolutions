# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from assertpy import assert_that
import math


def get_freq_from_file(file_name: str) -> dict[int, dict[str, int]]:
    return get_freq_from_list(convert_txt_to_list(file_name))


def convert_txt_to_list(file_name: str) -> list:
    with open(file_name) as binary_data:
        return [num.strip() for num in binary_data]


def get_freq_from_list(nums: list) -> dict[int, dict[str, int]]:
    freq_dict = {}
    for number in nums:
        for i, digit in enumerate(number.strip()):
            if i not in freq_dict:
                freq_dict[i] = {}
            freq_dict[i][digit] = freq_dict[i].get(digit, 0) + 1

    return freq_dict


def get_max_min_of_dict_in_dict(dict_of_dicts: dict[int, dict[str, int]]) -> (int, int):
    max_list = []
    min_list = []
    for i, freq in dict_of_dicts.items():
        max_list.append(max(freq, key=freq.get))
        min_list.append(min(freq, key=freq.get))
    return int("".join(max_list), 2), int("".join(min_list), 2)


def most_or_least_filter(number: str, freq_dict: dict, position, function) -> bool:
    if max(freq_dict.values()) == min(freq_dict.values()):
        if function is max:
            filter_d = '1'
        else:
            filter_d = '0'
    else:
        filter_d = function(freq_dict, key=freq_dict.get)
    return number[position] == filter_d


def get_most_or_least_common_num(list_num, pos_freq_dict, function) -> str:
    for i in range(len(pos_freq_dict)):
        list_num = list(filter(lambda num: most_or_least_filter(num, pos_freq_dict[i], i, function), list_num))
        if len(list_num) == 1:
            break
        pos_freq_dict = get_freq_from_list(list_num)
    return list_num[0]


if __name__ == '__main__':
    # PART1 TEST
    test_freq_dict = get_freq_from_file("data_test.txt")
    gamma_rate_d, eps_rate_d = get_max_min_of_dict_in_dict(test_freq_dict)

    power_cons = gamma_rate_d * eps_rate_d

    assert_that(power_cons).is_equal_to(198)

    # PART1 REAL
    real_freq_dict = get_freq_from_file("data_real.txt")
    gamma_rate_d, eps_rate_d = get_max_min_of_dict_in_dict(real_freq_dict)

    power_cons = gamma_rate_d * eps_rate_d
    assert_that(power_cons).is_not_equal_to(198)

    print(f"PART 1 real data {power_cons}")
    print(power_cons)

    # PART2 TEST
    num_list = convert_txt_to_list("data_test.txt")
    positional_freq = get_freq_from_list(num_list)
    oxy_rating_str = get_most_or_least_common_num(num_list, positional_freq, max)
    co2_rating_str = get_most_or_least_common_num(num_list, positional_freq, min)

    assert_that(oxy_rating_str).is_equal_to('10111')
    assert_that(co2_rating_str).is_equal_to('01010')

    life_support_rating = int(oxy_rating_str, 2) * int(co2_rating_str, 2)

    assert_that(life_support_rating).is_equal_to(230)

    # PART2 REAL
    num_list = convert_txt_to_list("data_real.txt")
    positional_freq = get_freq_from_list(num_list)
    oxy_rating_str = get_most_or_least_common_num(num_list, positional_freq, max)
    co2_rating_str = get_most_or_least_common_num(num_list, positional_freq, min)

    life_support_rating = int(oxy_rating_str, 2) * int(co2_rating_str, 2)

    assert_that(life_support_rating).is_not_equal_to(230)

    print(f"PART 2 REAL DATA is {life_support_rating}")
    print(life_support_rating)




