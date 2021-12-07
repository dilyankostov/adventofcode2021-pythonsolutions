# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from assertpy import assert_that


def extract_fish_dict_from_file(file_name: str) -> dict[int, int]:
    with open(file_name, 'r') as data_file:
        all_fishies: dict[int, int] = {}
        for age in data_file.readline().strip().split(','):
            all_fishies[int(age)] = all_fishies.get(int(age), 0) + 1
    return all_fishies


def age_fishies_n_days(fish_dict: dict[int, int], n: int) -> dict[int, int]:
    for i in range(n):
        new_fishies = dict(fish_dict)
        tryy=sorted(fish_dict.items(), reverse=True)

        for fish_age in range(8):
            new_fishies[fish_age] = fish_dict.get(fish_age + 1, 0)
        else:
            new_fishies[8] = fish_dict.get(0, 0)
            new_fishies[6] = new_fishies.get(6, 0) + fish_dict.get(0, 0)
        fish_dict = new_fishies
    return fish_dict


if __name__ == '__main__':
    # PART1 TEST
    fishies = extract_fish_dict_from_file("data_test.txt")
    assert_that(fishies).\
        is_equal_to({1: 1, 2: 1, 3: 2, 4: 1})
    aged_fishies = age_fishies_n_days(fishies, 18)
    assert_that(sum(aged_fishies.values())).is_equal_to(26)
    aged_fishies = age_fishies_n_days(fishies, 80)
    assert_that(sum(aged_fishies.values())).is_equal_to(5934)

    # PART1 REAL
    fishies = extract_fish_dict_from_file("data_real.txt")
    aged_fishies = age_fishies_n_days(fishies, 80)
    assert_that(sum(aged_fishies.values())).is_not_equal_to(5934)
    print("There are", sum(aged_fishies.values()), "fishies after 80 days")
    print(sum(aged_fishies.values()))

    # PART2 TEST
    fishies = extract_fish_dict_from_file("data_test.txt")
    aged_fishies = age_fishies_n_days(fishies, 256)
    assert_that(sum(aged_fishies.values())).is_equal_to(26984457539)

    # PART2 REAL
    fishies = extract_fish_dict_from_file("data_real.txt")
    aged_fishies = age_fishies_n_days(fishies, 256)
    assert_that(sum(aged_fishies.values())).is_not_equal_to(26984457539)
    print("There are", sum(aged_fishies.values()), "fishies after 80 days")
    print(sum(aged_fishies.values()))

    # 18 days 26 fish
    # 80 days 5934 fish





