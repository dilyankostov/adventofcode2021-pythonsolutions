# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from assertpy import assert_that
from collections import defaultdict


def get_vectors(file_name: str) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    with open(file_name, 'r') as data_file:
        points = []
        for entry in data_file:
            points_current = [point.strip().split(',') for point in entry.split("->")]
            point1 = tuple(map(lambda x: int(x), points_current[0]))
            point2 = tuple(map(lambda x: int(x), points_current[1]))
            points.append((point1, point2))

    return points


def get_result_from_all_points(coord_dict: dict[tuple[int], int]) -> int:
    return sum(map(lambda x: coord_dict.get(x) > 1, coord_dict))


def is_orthogonal(vectors: tuple[tuple[int], tuple[int]]) -> bool:
    (x1, y1), (x2, y2) = vectors
    return x1 == x2 or y1 == y2


def make_range(a: int, b: int, c: int, d: int):
    if a == b:
        return [a] * (abs(c - d) + 1)
    if a > b:
        return range(a, b - 1, -1)
    return range(a, b + 1)


def points(vectors: tuple[tuple[int, int], tuple[int, int]]) -> zip:
    (x1, y1), (x2, y2) = vectors
    return zip(make_range(x1, x2, y1, y2), make_range(y1, y2, x1, x2))


def find_overlapping_points(list_of_vectors, which_part="part1") -> dict[tuple[int, int], int]:
    orthogonal_overlaps = defaultdict(int)
    overlaps = defaultdict(int)
    for line in list_of_vectors:
        for point in points(line):
            overlaps[point] += 1
            orthogonal_overlaps[point] += is_orthogonal(line)
    if "2" in which_part:
        return overlaps
    else:
        return orthogonal_overlaps


def find_entries_larger_than_n(map_of_points: dict[tuple[int, int], int], n: int) -> int:
    return sum(overlap > n for overlap in map_of_points.values())


if __name__ == '__main__':
    # PART1 TEST
    vectors_current = get_vectors("data_test.txt")
    all_points = find_overlapping_points(vectors_current)
    answer = find_entries_larger_than_n(all_points, 1)
    assert_that(answer).is_equal_to(5)

    # PART1 REAL
    vectors_current = get_vectors("data_real.txt")
    all_points = find_overlapping_points(vectors_current)
    answer = find_entries_larger_than_n(all_points, 1)
    assert_that(answer).is_not_equal_to(5)
    print(answer)

    # PART2 TEST
    vectors_current = get_vectors("data_test.txt")
    all_points = find_overlapping_points(vectors_current, "part2")
    answer = find_entries_larger_than_n(all_points, 1)
    assert_that(answer).is_equal_to(12)

    # PART2 REAL
    vectors_current = get_vectors("data_real.txt")
    all_points = find_overlapping_points(vectors_current, "part2")
    answer = find_entries_larger_than_n(all_points, 1)
    assert_that(answer).is_not_equal_to(12)
    print(answer)







