# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from assertpy import assert_that
from collections import defaultdict


def extract_codes_from_file(file_name: str) -> dict[str, set[str, ...]]:
    extracted_paths = defaultdict(lambda: set())
    with open(file_name, 'r') as data_file:
        for line in data_file:
            p1, p2 = line.strip().split('-')
            if p2 != 'start':
                extracted_paths[p1].add(p2)
            if p1 != 'start':
                extracted_paths[p2].add(p1)
    return extracted_paths


def recurse_connections(
        connections: dict[str, set[str, ...]],
        path=None,
        second_repeats: bool = True,
) -> list[list[str]]:
    if path is None:
        path = ['start']
    paths = list()
    for to_ in connections.get(path[-1]):
        if to_ == 'end':
            paths.append(path + ['end'])
            continue
        elif to_ in path and to_.islower() and not second_repeats:
            continue
        if to_.islower() and to_ in path:
            paths.extend(recurse_connections(connections, path + [to_], False))
        else:
            paths.extend(recurse_connections(connections, path + [to_], second_repeats))

    return paths


if __name__ == '__main__':
    # PART1 TEST
    corridors = extract_codes_from_file("data_test.txt")
    all_paths = recurse_connections(corridors, second_repeats=False)
    assert_that(len(all_paths)).is_equal_to(10)

    # PART1 TEST2
    corridors = extract_codes_from_file("data_test2.txt")
    all_paths = recurse_connections(corridors, second_repeats=False)
    assert_that(len(all_paths)).is_equal_to(19)

    # PART1 TEST3
    corridors = extract_codes_from_file("data_test3.txt")
    all_paths = recurse_connections(corridors, second_repeats=False)
    assert_that(len(all_paths)).is_equal_to(226)

    # PART1 REAL
    corridors = extract_codes_from_file("data_real.txt")
    all_paths = recurse_connections(corridors, second_repeats=False)
    print(len(all_paths))

    # PART2 TEST
    corridors = extract_codes_from_file("data_test.txt")
    all_paths = recurse_connections(corridors)
    assert_that(len(all_paths)).is_equal_to(36)

    # PART2 TEST2
    corridors = extract_codes_from_file("data_test2.txt")
    all_paths = recurse_connections(corridors)
    assert_that(len(all_paths)).is_equal_to(103)

    # PART2 TEST3
    corridors = extract_codes_from_file("data_test3.txt")
    all_paths = recurse_connections(corridors)
    assert_that(len(all_paths)).is_equal_to(3509)

    # PART2 REAL
    corridors = extract_codes_from_file("data_real.txt")
    all_paths = recurse_connections(corridors)
    print(len(all_paths))
