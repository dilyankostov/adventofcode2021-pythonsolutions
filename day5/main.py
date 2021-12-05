# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from assertpy import assert_that


def generate_inbetween_points(vector: tuple[tuple[int, ...], tuple[int, ...]]) \
        -> list[tuple[int, ...]]:
    ((x1, y1), (x2, y2)) = vector
    points_inbetween = []
    if x1 > x2:
        x_diff = -1
    elif x1 < x2:
        x_diff = 1
    else:
        x_diff = 0
    if y1 > y2:
        y_diff = -1
    elif y1 < y2:
        y_diff = 1
    else:
        y_diff = 0
    x_prev, y_prev = x1, y1
    for i in range(max(abs(x1-x2) + 1, abs(y1-y2) + 1)):
        points_inbetween.append((x_prev, y_prev))
        x_prev = x_prev + x_diff
        y_prev = y_prev + y_diff
    return points_inbetween


def get_vectors(file_name: str) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    with open(file_name, 'r') as data_file:
        points = []
        for entry in data_file:
            points_current = [point.strip().split(',') for point in entry.split("->")]
            point1 = tuple(map(lambda x: int(x), points_current[0]))
            point2 = tuple(map(lambda x: int(x), points_current[1]))
            points.append((point1, point2))

    return points


def map_only_straight_vec_to_map(vectors: list[tuple[tuple[int, ...], tuple[int, ...]]]) -> dict[tuple[int], int]:
    coord_dict = {}
    for vector in vectors:
        ((x1, y1), (x2, y2)) = vector
        if x1 == x2 or y1 == y2:
            points = generate_inbetween_points(vector)
            for point in points:
                coord_dict[point] = coord_dict.get(point, 0) + 1
    return coord_dict


def map_vec_to_points(vectors: list[tuple[tuple[int, ...], tuple[int, ...]]]) -> dict[tuple[int], int]:
    coord_dict = {}
    for vector in vectors:
        points = generate_inbetween_points(vector)
        for point in points:
            coord_dict[point] = coord_dict.get(point, 0) + 1
    return coord_dict


def get_result_from_all_points(coord_dict: dict[tuple[int], int]) -> int:
    return sum(map(lambda x: coord_dict.get(x) > 1, coord_dict))


if __name__ == '__main__':
    # PART1 TEST
    vectors_current = get_vectors("data_test.txt")
    all_points = map_only_straight_vec_to_map(vectors_current)
    answer = get_result_from_all_points(all_points)
    assert_that(answer).is_equal_to(5)

    # PART1 REAL
    vectors_current = get_vectors("data_real.txt")
    all_points = map_only_straight_vec_to_map(vectors_current)
    answer = get_result_from_all_points(all_points)
    assert_that(answer).is_not_equal_to(5)
    print(answer)

    # PART2 TEST
    vectors_current = get_vectors("data_test.txt")
    all_points = map_vec_to_points(vectors_current)
    answer = get_result_from_all_points(all_points)
    assert_that(answer).is_equal_to(12)

    # PART2 REAL
    vectors_current = get_vectors("data_real.txt")
    all_points = map_vec_to_points(vectors_current)
    answer = get_result_from_all_points(all_points)
    assert_that(answer).is_not_equal_to(12)
    print(answer)







