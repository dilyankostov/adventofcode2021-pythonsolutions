# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from assertpy import assert_that
import heapq
from numpy import base_repr


def extract_data_from_file(file_name: str) -> dict[tuple[int, int], int]:
    data_map: dict[tuple[int, int], int] = {}
    with open(file_name, 'r') as data_file:
        for i, line in enumerate(data_file):
            for ii, c, in enumerate(line.strip()):
                data_map[(i, ii)] = int(c)
    return data_map


def get_adjacent_iteratively(coord, height, width) -> tuple[int, int]:
    for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        (x, y) = coord
        if 0 <= x + i <= width and 0 <= y + j <= height:
            yield x + i, y + j


def search_adjasent(coord_map: dict[tuple[int,int], int], start_coord: tuple[int, int] = (0, 0)) -> int:
    height_map: int = max(map(lambda i: i[1], coord_map))
    width_map: int = max(map(lambda i: i[0], coord_map))
    sq: list = [(0, start_coord)]
    visited: set = {start_coord}
    while True:
        min_p, (x, y) = heapq.heappop(sq)
        if (x, y) == (height_map, width_map):
            return min_p
        for (x2, y2) in get_adjacent_iteratively((x, y), height=height_map, width=width_map):
            if (x2, y2) not in visited:
                visited.add((x2, y2))
                heapq.heappush(sq, (min_p + coord_map[x2, y2], (x2, y2)))


def expand_map(coord_map):
    height_map: int = max(map(lambda i: i[1], coord_map)) + 1
    width_map: int = max(map(lambda i: i[0], coord_map)) + 1
    new_map = {}
    for i in range(5):
        for j in range(5):
            new_map = new_map | \
                      {
                          (width_map * i + x, height_map * j + y): int(base_repr(v + i + j, 9)) % 10 or 9
                          for ((x, y), v)
                          in coord_map.items()
                      }
    return new_map


if __name__ == '__main__':
    # PART1 TEST
    chitons_map = extract_data_from_file("data_test.txt")
    answer = search_adjasent(chitons_map)
    assert_that(answer).is_equal_to(40)

    # PART1 REAL
    chitons_map = extract_data_from_file("data_real.txt")
    answer = search_adjasent(chitons_map)
    assert_that(answer).is_not_equal_to(40)

    # PART2 TEST
    chitons_map = extract_data_from_file("data_test.txt")
    chitons_expanded = expand_map(chitons_map)
    answer = search_adjasent(chitons_expanded)
    assert_that(answer).is_equal_to(315)

    # PART2 REAL
    chitons_map = extract_data_from_file("data_real.txt")
    chitons_expanded = expand_map(chitons_map)
    answer = search_adjasent(chitons_expanded)
    assert_that(answer).is_not_equal_to(315)
    print(answer)






