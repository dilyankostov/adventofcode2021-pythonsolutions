# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from assertpy import assert_that
import heapq
from numpy import base_repr
import time
start_time = time.time()


def extract_data_from_file(file_name: str) -> tuple[dict[tuple[int, int], int], int, int]:
    data_map: dict[tuple[int, int], int] = {}
    with open(file_name, 'r') as data_file:
        for x, line in enumerate(data_file):
            for y, c, in enumerate(line.strip()):
                data_map[(x, y)] = int(c)
    return data_map, x, y


def get_adjacent_iteratively(x, y, height, width) -> tuple[int, int]:
    for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x2, y2 = x + i, y + j
        if 0 <= x2 <= width and 0 <= y2 <= height:
            yield x2, y2


def search_adjasent(coord_map: dict[tuple[int,int], int],
                    height: int, width: int,
                    start_coord: tuple[int, int] = (0, 0)) -> int:
    sq: list = [(0, start_coord)]
    visited: set = {start_coord}
    while True:
        min_p, (x, y) = heapq.heappop(sq)
        if x == height and y == width:
            return min_p
        for x2, y2 in get_adjacent_iteratively(x, y, height=height, width=width):
            if (x2, y2) not in visited:
                visited.add((x2, y2))
                heapq.heappush(sq, (min_p + coord_map[x2, y2], (x2, y2)))


def expand_map(coord_map: dict[tuple[int,int], int], height: int, width: int):
    new_map = {}
    for i in range(5):
        for j in range(5):
            for ((x, y), v) in coord_map.items():
                new_map[((width + 1) * i + x, (height + 1) * j + y)] = int(base_repr(v + i + j, 9)) % 10 or 9
    return new_map


if __name__ == '__main__':
    # PART1 TEST
    chitons_map, map_x, map_y = extract_data_from_file("data_test.txt")
    answer = search_adjasent(chitons_map, height=map_y, width=map_x)
    assert_that(answer).is_equal_to(40)

    # PART1 REAL
    chitons_map, map_x, map_y = extract_data_from_file("data_real.txt")
    answer = search_adjasent(chitons_map, height=map_y, width=map_x)
    assert_that(answer).is_not_equal_to(40)

    # PART2 TEST
    chitons_map, map_x, map_y = extract_data_from_file("data_test.txt")
    chitons_expanded = expand_map(chitons_map, height=map_y, width=map_x)
    answer = search_adjasent(chitons_expanded, height=(map_y + 1) * 5 - 1, width=(map_x + 1) * 5 - 1)
    assert_that(answer).is_equal_to(315)

    # PART2 REAL
    print("--- %s seconds ---" % (round(time.time() - start_time, 2)))
    chitons_map, map_x, map_y = extract_data_from_file("data_real.txt")
    print("--- %s seconds ---" % (round(time.time() - start_time, 2)))
    chitons_expanded = expand_map(chitons_map, height=map_y, width=map_x)
    print("--- %s seconds ---" % (round(time.time() - start_time, 2)))
    answer = search_adjasent(chitons_expanded, height=(map_y + 1) * 5 - 1, width=(map_x + 1) * 5 - 1)
    print("--- %s seconds ---" % (round(time.time() - start_time, 2)))
    assert_that(answer).is_not_equal_to(315)
    print(answer)






