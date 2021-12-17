# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import Iterator
from assertpy import assert_that
from numpy import base_repr


def extract_data_from_file(file_name: str) -> Iterator:
    with open(file_name, 'r') as data_file:
        return bin(int('1'+data_file.readline().strip(), 16))[3:]


def str_iter_n(iterable: Iterator, iterator_counter: int, n: int) -> tuple[str, int]:
    total = ""
    for i in range(n):
        total += next(iterable)
        iterator_counter += 1
    return total, iterator_counter


def literal_packet(iterable: Iterator, iter_counter: int = 6) -> tuple[int, int]:
    number = ""
    while True:
        first_v, iter_counter = str_iter_n(iterable, iter_counter, 1)
        value, iter_counter = str_iter_n(iterable, iter_counter, 4)
        number += value
        if first_v == '0':
            break
    number = int(number, 2)
    # rest, iter_counter = str_iter_n(iterable, iter_counter, 4 - (iter_counter % 4))
    return number, iter_counter


def read_packet(iterable: Iterator, total_counter: int = 0) -> tuple[int, int, int]:
    iter_counter = 0
    packet_version, iter_counter = str_iter_n(itr, iter_counter, 3)
    packet_version_sum = int(packet_version, 2)
    packet_id, iter_counter = str_iter_n(itr, iter_counter, 3)
    if int(packet_id, 2) == 4:
        secret_n, iter_counter = literal_packet(itr, iter_counter)
        return secret_n, iter_counter, packet_version_sum
    else:
        length_type, iter_counter = str_iter_n(iterable, iter_counter, 1)
        if length_type == '0':
            sub_len, iter_counter = str_iter_n(iterable, iter_counter, 15)
            sub_len = int(sub_len, 2)
            sub_read = 0
            num = 0
            while sub_len > sub_read:
                read_num, read_iters, read_pack_v = read_packet(itr)
                packet_version_sum += read_pack_v
                sub_read += read_iters
                num += read_num
            return num, iter_counter + sub_read, packet_version_sum
        else:
            sub_len, iter_counter = str_iter_n(iterable, iter_counter, 11)
            sub_len = int(sub_len, 2)
            sub_read = 0
            num = 0
            for i in range(sub_len):
                read_num, read_iters, read_pack_v = read_packet(itr)
                packet_version_sum += read_pack_v
                sub_read += read_iters
                num += read_num
            return num, iter_counter + sub_read, packet_version_sum


if __name__ == '__main__':
    # PART1 TEST
    itr = extract_data_from_file("data_test_literal_packet_2021.txt")
    itr = iter(itr)
    answer = read_packet(itr)
    assert_that(answer[0]).is_equal_to(2021)

    itr = extract_data_from_file("data_test_operational1.txt")
    itr = iter(itr)
    answer = read_packet(itr)
    assert_that(answer[0]).is_equal_to(30)

    itr = extract_data_from_file("data_test_operational2.txt")
    itr = iter(itr)
    answer = read_packet(itr)
    assert_that(answer[0]).is_equal_to(6)

    itr = extract_data_from_file("data_test_packet_v_sum1.txt")
    itr = iter(itr)
    answer = read_packet(itr)
    assert_that(answer[2]).is_equal_to(16)
    itr = extract_data_from_file("data_test_packet_v_sum2.txt")
    itr = iter(itr)
    answer = read_packet(itr)
    assert_that(answer[2]).is_equal_to(12)
    itr = extract_data_from_file("data_test_packet_v_sum3.txt")
    itr = iter(itr)
    answer = read_packet(itr)
    assert_that(answer[2]).is_equal_to(23)
    itr = extract_data_from_file("data_test_packet_v_sum4.txt")
    itr = iter(itr)
    answer = read_packet(itr)
    assert_that(answer[2]).is_equal_to(31)

    # PART 1 REAL
    itr = extract_data_from_file("data_real.txt")
    itr = iter(itr)
    answer = read_packet(itr)
    print(answer)
