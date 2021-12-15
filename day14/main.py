# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from assertpy import assert_that
import re
from collections import defaultdict


def extract_instr_from_file(file_name: str) -> tuple[dict[tuple[str, str], int], dict[tuple[str, str], str], str]:
    instructions: dict[tuple[str, str], str] = {}
    start_comb: dict[tuple[str, str], int] = {}
    with open(file_name, 'r') as data_file:
        for line in data_file:
            if '->' in line:
                pair, in_ = re.findall(r'(.*) -> (.*)', line)[0]
                instructions[tuple(pair)] = in_.strip()
            elif line.strip().isalpha():
                init_poly = line.strip()
                for i in range(len(line.strip()) - 1):
                    start_comb[(line[i], line[i+1])] = start_comb.get((line[i], line[i+1]), 0) + 1
    return start_comb, instructions, init_poly


def insert_once(poly: dict[tuple[str, str], int], insertions: dict[tuple[str, str], str]) -> dict[tuple[str, str], int]:
    if not poly:
        return poly
    poly_n = dict(poly)
    for ins_, v in insertions.items():
        if ins_ in poly:
            poly_n[(ins_[0], v)] = poly_n.get((ins_[0], v), 0) + poly[ins_]
            poly_n[(v, ins_[1])] = poly_n.get((v, ins_[1]), 0) + poly[ins_]
            poly_n[ins_] = poly_n.get(ins_, 0) - poly[ins_]

    return poly_n


def repeat_n_insertions(poly: dict[tuple[str, str], int],
                        instr: dict[tuple[str, str], str],
                        n: int
                        ) -> dict[tuple[str, str], int]:
    for i in range(n):
        poly = insert_once(poly, instr)
        # print(f"step {i}")
    return poly


def find_letter_freq(poly: dict[tuple[str, str], int], poly_start: str) -> dict[str, int]:
    freq_2n = defaultdict(lambda: 0)
    for (l1, l2), freq_n in poly.items():
        freq_2n[l1] += poly[(l1, l2)]
        freq_2n[l2] += poly[(l1, l2)]
    freq_2n[poly_start[0]] += 1
    freq_2n[poly_start[-1]] += 1
    freq = {k: v/2 for (k, v) in freq_2n.items()}
    return freq


if __name__ == '__main__':
    # PART1 TEST
    start_polymer, insertion_instr, start_polymer_str = extract_instr_from_file("data_test.txt")
    new_poly = repeat_n_insertions(start_polymer, insertion_instr, 10)
    n_letters = sum(new_poly.values()) + 1
    assert_that(n_letters).is_equal_to(3073)
    l_freq = find_letter_freq(new_poly, start_polymer_str)
    extr_diff = max(l_freq.values()) - min(l_freq.values())
    assert_that(extr_diff).is_equal_to(1588)

    # PART1 REAL
    start_polymer, insertion_instr, start_polymer_str = extract_instr_from_file("data_real.txt")
    new_poly = repeat_n_insertions(start_polymer, insertion_instr, 10)
    l_freq = find_letter_freq(new_poly, start_polymer_str)
    max_c, min_c = max(l_freq, key=l_freq.get), max(l_freq, key=l_freq.get)
    extr_diff = max(l_freq.values()) - min(l_freq.values())
    print(f"Most freq letter: {max_c}, least freq: {min_c}. Their diff is {extr_diff}")

    # PART2 TEST
    start_polymer, insertion_instr, start_polymer_str = extract_instr_from_file("data_test.txt")
    new_poly = repeat_n_insertions(start_polymer, insertion_instr, 40)
    l_freq = find_letter_freq(new_poly, start_polymer_str)
    max_c, min_c = max(l_freq, key=l_freq.get), min(l_freq, key=l_freq.get)
    assert_that((max_c, min_c)).is_equal_to(('B', 'H'))
    extr_diff = max(l_freq.values()) - min(l_freq.values())
    print(f"Most freq letter: {max_c}, least freq: {min_c}. Their diff is {extr_diff}")
    assert_that(extr_diff).is_equal_to(2188189693529)

    # PART2 REAL
    start_polymer, insertion_instr, start_polymer_str = extract_instr_from_file("data_real.txt")
    new_poly = repeat_n_insertions(start_polymer, insertion_instr, 40)
    l_freq = find_letter_freq(new_poly, start_polymer_str)
    max_c, min_c = max(l_freq, key=l_freq.get), min(l_freq, key=l_freq.get)
    extr_diff = max(l_freq.values()) - min(l_freq.values())
    print(f"Most freq letter: {max_c}, least freq: {min_c}. Their diff is {extr_diff}")

