# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from assertpy import assert_that
import re


def extract_data_from_file(file_name: str) -> list:
    with open(file_name, 'r') as data_file:
        limits = re.search(r"x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", data_file.readline()).groups()
        return [int(i) for i in limits]


def shoot(dx, dy, x1, x2, y1, y2, x=0, y=0):
    if x in range(x1, x2 + 1) and y in range(y2, y1 - 1, -1):
        return True
    if x > x2 or y < y1:
        return False
    return shoot(max(0, dx - 1), dy - 1, x1, x2, y1, y2, x+dx, y+dy)


def shoot_shots(x1, x2, y1, y2):
    total = 0
    for dx in range(1, t_x2 + 1):
        for dy in range(t_y1, -t_y1):
            total += shoot(dx, dy, x1, x2, y1, y2)
    return total


if __name__ == '__main__':
    # PART1 TEST
    t_x1, t_x2, t_y1, t_y2 = extract_data_from_file("data_test.txt")
    # from maths, we know that if it starts with velocity v and then it's height is v, v + v-1, v + v-1 + v-2... + 1
    # and there is a formula that x + x-1 +... 1 = x*(x+1)/2. The max height would go up then hit y=0, then hit - (v+1)
    # so if you hit y0 (negative) directly after the horiz line, you have started with |y0|-1 speed = y0+1.
    # So hitting y0 when y0 is negative leads to max height (y0+1)(y0+1-1)/2=y0*(y0+1)/2.
    max_y = t_y1*(t_y1+1)//2
    assert_that(max_y).is_equal_to(45)
    answer = shoot_shots(t_x1, t_x2, t_y1, t_y2)
    assert_that(answer).is_equal_to(112)

    # PART1 REAL
    t_x1, t_x2, t_y1, t_y2 = extract_data_from_file("data_real.txt")
    max_y = t_y1*(t_y1+1)//2
    print(max_y)
    answer = shoot_shots(t_x1, t_x2, t_y1, t_y2)
    print(answer)
