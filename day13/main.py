# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from assertpy import assert_that
import re


def extract_codes_from_file(file_name: str) -> tuple[set[tuple[int, ...]], list]:
    coords = set()
    instructions = []
    with open(file_name, 'r') as data_file:
        for line in data_file:
            if ',' in line:
                coords.add(tuple(int(i) for i in line.strip().split(',')))
            elif '=' in line:
                axis, n = re.findall(r'fold along (.*)=(.*)', line)[0]
                instructions.append((axis, int(n.strip())))
    return coords, instructions


def fold_once(coord_map, fold):
    new_map = set()
    if fold[0] == 'x':
        axis = 0
    else:
        axis = 1
    for coord_ in coord_map:
        x, y = coord_
        if coord_[axis] < fold[1]:
            new_map.add(coord_)
        else:
            if fold[0] == 'x':
                new_map.add((fold[1] - (x - fold[1]), y))
            else:
                new_map.add((x, fold[1] - (y - fold[1])))
    return new_map


def fold_all(coord_map, all_folds):
    for fold in all_folds:
        coord_map = fold_once(coord_map, fold)
    return coord_map


def print_all(coord_map):
    for y in range(max(map(lambda i: i[1], coord_map)) + 1):
        for x in range(max(map(lambda i: i[0], coord_map)) + 1):
            if (x, y) in coord_map:
                print('#', end='')
            else:
                print('.', end='')
        print()


if __name__ == '__main__':
    # PART1 TEST
    points, folds = extract_codes_from_file("data_test.txt")
    n_points = len(fold_once(points, folds[0]))
    assert_that(n_points).is_equal_to(17)

    # PART1 REAL
    points, folds = extract_codes_from_file("data_real.txt")
    n_points = len(fold_once(points, folds[0]))
    assert_that(n_points).is_not_equal_to(17)
    print(n_points)

    # PART2 TEST
    points, folds = extract_codes_from_file("data_test.txt")
    fold_all(points, folds)

    # PART2 REAL
    points, folds = extract_codes_from_file("data_real.txt")
    print_all(fold_all(points, folds))
