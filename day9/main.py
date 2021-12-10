# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from assertpy import assert_that
from numpy import prod


def extract_codes_from_file(file_name: str) -> dict[tuple[int, int], int]:
    codes_map = {}
    with open(file_name, 'r') as data_file:
        for i, line in enumerate(data_file):
            for ii, value in enumerate(list(line.strip())):
                codes_map[(i, ii)] = int(value)
    return codes_map


def is_it_vent(coord_map: dict[tuple[int, int], int], i: int, ii: int, value: int) -> bool:
    return coord_map.get((i + 1, ii), 100) > value and coord_map.get((i, ii + 1), 100) > value and \
            coord_map.get((i - 1, ii), 100) > value and coord_map.get((i, ii - 1), 100) > value


def is_coord_in_flow(value_to_compare: int, value: int, not_value: int):
    return False if value_to_compare is None else value_to_compare > value and value_to_compare != not_value


def where_is_the_flow(coord_map: dict[tuple[int, int], int], coord: tuple[int, int]):
    i, ii = coord
    current_value = coord_map[i, ii]
    flow_source = {}
    coords_to_search = [
        (i + 1, ii),
        (i - 1, ii),
        (i, ii + 1),
        (i, ii - 1),
    ]
    for coord_search_ in coords_to_search:
        if is_coord_in_flow(coord_map.get(coord_search_, None), current_value, 9):
            flow_source[coord_search_] = coord_map[coord_search_]
    return flow_source


def recurse_search_for_point(coord_map, coord):
    flow_points = where_is_the_flow(coord_map, coord)
    more_flow_points = {}
    for flow_point in flow_points:
        more_flow_points = more_flow_points | recurse_search_for_point(coord_map, flow_point)
    return flow_points | more_flow_points | {coord: coord_map[coord]}


def get_lowest_points(coord_map: dict[tuple[int, int], int]) -> dict[tuple[int, int], int]:
    lowest_n = {}
    for (i, ii), value in coord_map.items():
        if is_it_vent(coord_map, i, ii, value):
            lowest_n[(i, ii)] = value
    return lowest_n


if __name__ == '__main__':
    # PART1 TEST
    floor_map = extract_codes_from_file("data_test.txt")
    vents = get_lowest_points(floor_map)
    assert_that(sorted(vents.values())).is_equal_to(sorted([1, 0, 5, 5]))
    answer = sum(vents.values()) + len(vents.values())
    assert_that(answer).is_equal_to(15)

    # PART1 REAL
    floor_map = extract_codes_from_file("data_real.txt")
    vents = get_lowest_points(floor_map)
    assert_that(sorted(vents.values())).is_not_equal_to(sorted([1, 0, 5, 5]))
    answer = sum(vents.values()) + len(vents.values())
    assert_that(answer).is_not_equal_to(15)
    print(answer)

    # PART2 TEST
    floor_map = extract_codes_from_file("data_test.txt")
    vents = get_lowest_points(floor_map)
    assert_that(sorted(vents.values())).is_equal_to(sorted([1, 0, 5, 5]))
    answer = sum(vents.values()) + len(vents.values())
    assert_that(answer).is_equal_to(15)
    all_basins = []
    for vent in vents:
        basin_points = recurse_search_for_point(floor_map, vent)
        print(basin_points)
        all_basins.append(basin_points)
    top_3 = sorted(all_basins, key=len, reverse=True)[:3]
    answer = prod([len(b) for b in top_3])
    assert_that(answer).is_equal_to(1134)

    # PART2 REAL
    floor_map = extract_codes_from_file("data_real.txt")
    vents = get_lowest_points(floor_map)
    assert_that(sorted(vents.values())).is_not_equal_to(sorted([1, 0, 5, 5]))
    all_basins = []
    for vent in vents:
        basin_points = recurse_search_for_point(floor_map, vent)
        print(basin_points)
        all_basins.append(basin_points)
    top_3 = sorted(all_basins, key=len, reverse=True)[:3]
    answer = prod([len(b) for b in top_3])
    assert_that(answer).is_not_equal_to(1134)
    print(answer)



