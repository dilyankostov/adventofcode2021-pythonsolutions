# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math
import operator
from typing import Any
from assertpy import assert_that
import re
import numpy
from collections import defaultdict

def extract_data_from_file(file_name: str) -> list:
    with open(file_name, 'r') as data_file:
        return [(int(x1), int(x2)) for x1, x2 in [x.split("..") for x in re.findall(r"target area: x=(.*), y=(.*)",
                                                                                    data_file.readline().strip())[0]]]


def next_x(velocity: int) -> int:
    return velocity - numpy.sign(velocity)


def next_y(velocity: int) -> int:
    return velocity - 1


def calc_x(x1, x2):
    # only pos case
    target = range(x1, x2 + 1)
    winners = defaultdict(list)
    for init_vel in range(numpy.sign(x2), x2 + numpy.sign(x2), numpy.sign(x2)):
        next_pos = init_vel
        vel = init_vel
        for n_steps in range(1, 200):
            if next_pos in target:
                winners[init_vel].append(n_steps)
            vel = next_x(vel)
            next_pos = next_pos + vel
            if next_pos > x2:
                break
    return winners


def calc_y(y1, y2):
    # only pos case
    target = range(y2, y1 + numpy.sign(y2), numpy.sign(y2))
    winners = defaultdict(list)
    for init_vel in range(min(0, y1, y2), max(abs(y1), abs(y2)) + 1):
        next_pos = init_vel
        max_pos = max(0, next_pos)
        vel = init_vel
        n_steps = 1
        while True:
            if next_pos in target:
                winners[init_vel].append((n_steps, max_pos))
            vel = vel - 1
            next_pos = next_pos + vel
            max_pos = max(max_pos, next_pos)
            n_steps += 1
            if next_pos < min(y1, y2):
                break
    return winners


if __name__ == '__main__':
    # PART1 TEST
    (t_x1, t_x2), (t_y1, t_y2) = extract_data_from_file("data_test.txt")
    possible_x = calc_x(t_x1, t_x2)
    possible_y = calc_y(t_y1, t_y2)
    answer_p1 = possible_y[max(possible_y)]
    assert_that(answer_p1[0][1]).is_equal_to(45)
    mixed = set()
    for y, v in possible_y.items():
        for point in v:
            for x, v2 in possible_x.items():
                if point[0] in v2:
                    mixed.add((x, y))
    assert_that(len(mixed)).is_equal_to(112)

    # PART1 REAL
    (t_x1, t_x2), (t_y1, t_y2) = extract_data_from_file("data_real.txt")
    possible_x = calc_x(t_x1, t_x2)
    possible_y = calc_y(t_y1, t_y2)
    answer = possible_y[max(possible_y)]
    print(answer)
    mixed = set()
    for y, v in possible_y.items():
        for point in v:
            for x, v2 in possible_x.items():
                if point[0] in v2:
                    mixed.add((x, y))
    # assert_that(len(mixed)).is_greater_than(1876)
    print(len(mixed))
