# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from assertpy import assert_that
from statistics import median


def extract_codes_from_file(file_name: str) -> dict[tuple[int, int], int]:
    extracted_codes = {}
    with open(file_name, 'r') as data_file:
        for i, line in enumerate(data_file):
            for ii, c in enumerate(line.strip()):
                extracted_codes[(i, ii)] = int(c)
    return extracted_codes


def incrase_adj(coord_map, coord, changed_points):
    for coord_change_ in get_adj_points(coord):
        if coord_change_ in coord_map:
            coord_map[coord_change_] = coord_map[coord_change_] + 1


def get_adj_points(coord):
    i, ii = coord
    return [
        (i + 1, ii),
        (i + 1, ii + 1),
        (i + 1, ii - 1),
        (i - 1, ii),
        (i - 1, ii + 1),
        (i - 1, ii - 1),
        (i, ii + 1),
        (i, ii - 1),
    ]


def recurse_incrase_adj(coord_map, coord, changed_points=None) -> set[tuple[int, int]]:
    if changed_points is None:
        changed_points = set()
    if coord in coord_map and coord_map.get(coord, 0) > 9 and coord not in changed_points:
        changed_points.add(coord)
        incrase_adj(coord_map, coord, changed_points)
        coord_map[coord] = 0
        for adj_p in get_adj_points(coord):
            changed_points = changed_points | recurse_incrase_adj(coord_map, adj_p, changed_points)
        coord_map[coord] = 0
    return changed_points


def add_one_to_all(coord_map: dict[tuple[int, int], int]) -> dict[tuple[int, int], int]:
    for x in range(max(map(lambda x: x[0], coord_map)) + 1):
        for y in range(max(map(lambda x: x[1], coord_map)) + 1):
            coord_map[(x, y)] = coord_map.get((x, y), 0) + 1
    return coord_map


def flash_all(coord_map: dict[tuple[int, int], int]) -> set[tuple[int, int]]:
    coords_blown = set()
    for x in range(max(map(lambda x: x[0], coord_map)) + 1):
        for y in range(max(map(lambda x: x[1], coord_map)) + 1):
            coords_blown = coords_blown | (recurse_incrase_adj(coord_map, (x, y)))
    return coords_blown


def print_all_map(coord_map):
    for x in range(max(map(lambda x: x[0], coord_map)) + 1):
        for y in range(max(map(lambda x: x[1], coord_map)) + 1):
            print(coord_map[(x, y)], end='')
        print('')
    print(f'YEAR END')


def zero_all_flashed(coord_map: dict[tuple[int, int], int], flashed_points):
    for flashed_p_ in flashed_points:
        coord_map[flashed_p_] = 0


def do_n_years(coord_map: dict[tuple[int, int], int], years: int) -> int:
    all_flashes = 0
    for i in range(years):
        add_one_to_all(coord_map)
        flashed_points = flash_all(coord_map)
        zero_all_flashed(coord_map, flashed_points)
        all_flashes += len(flashed_points)
        # print_all_map(coord_map)
    return all_flashes


def find_n_years(coord_map: dict[tuple[int, int], int]) -> int:
    i = 0
    while True:
        i += 1
        add_one_to_all(coord_map)
        flashed_points = flash_all(coord_map)
        zero_all_flashed(coord_map, flashed_points)
        if all(v == 0 for v in coord_map.values()):
            return i


if __name__ == '__main__':
    # PART1 TEST
    octopuses = extract_codes_from_file("data_test.txt")
    do_n_years(octopuses, 2)
    assert_that(extract_codes_from_file("test_after_2days.txt")).is_equal_to(octopuses)
    octopuses = extract_codes_from_file("data_test.txt")
    flashed_octopuses = do_n_years(octopuses, 100)
    assert_that(flashed_octopuses).is_equal_to(1656)
    print(flashed_octopuses)

    # PART1 REAL
    octopuses = extract_codes_from_file("data_real.txt")
    flashed_octopuses = do_n_years(octopuses, 100)
    print(flashed_octopuses)

    # PART2 TEST
    octopuses = extract_codes_from_file("data_test.txt")
    years = find_n_years(octopuses)
    assert_that(years).is_equal_to(195)

    # PART2 REAL
    octopuses = extract_codes_from_file("data_real.txt")
    years = find_n_years(octopuses)
    print(years)
