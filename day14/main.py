# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from assertpy import assert_that
import re
from collections import defaultdict


def extract_instr_from_file(file_name: str) -> tuple[list[str], dict[tuple[str, str], str]]:
    instructions: dict[tuple[str, str], str] = {}
    start_comb: list[str] = []
    with open(file_name, 'r') as data_file:
        for line in data_file:
            if '->' in line:
                pair, in_ = re.findall(r'(.*) -> (.*)', line)[0]
                instructions[tuple(pair)] = in_.strip()
            elif line.strip().isalpha():
                start_comb = list(line.strip())
    return start_comb, instructions


def insert_once(start: list[str], instr: dict[tuple[str, str], str]):
    if len(start) < 2:
        return start
    s_new = list()
    next_c = start[0]
    for i in range(len(start) - 1):
        prev_c = next_c
        next_c = start[i+1]
        s_new.append(prev_c)
        instr_result = instr.get((prev_c, next_c), None)
        if instr_result:
            s_new.append(instr_result)
    s_new.append(next_c)
    return s_new


def repeat_n_insertions(start_poly: list[str], instr: dict[tuple[str, str], str], n: int) -> list[str]:
    polymer = list(start_poly)
    for i in range(n):
        polymer = insert_once(polymer, instr)
        print(f"step {i} and polymer is {len(polymer)} long")
    return polymer


def find_letter_freq(letter_list: list[str]) -> dict[str, int]:
    freq = defaultdict(lambda: 0)
    for c_ in letter_list:
        freq[c_] += 1
    return freq


if __name__ == '__main__':
    # PART1 TEST
    start_polymer, insertion_instr = extract_instr_from_file("data_test.txt")
    new_poly = repeat_n_insertions(start_polymer, insertion_instr, 10)
    assert_that(len(new_poly)).is_equal_to(3073)
    l_freq = find_letter_freq(new_poly)
    extr_diff = max(l_freq.values()) - min(l_freq.values())
    assert_that(extr_diff).is_equal_to(1588)

    # PART1 TEST
    start_polymer, insertion_instr = extract_instr_from_file("data_real.txt")
    new_poly = repeat_n_insertions(start_polymer, insertion_instr, 10)
    l_freq = find_letter_freq(new_poly)
    max_c, min_c = max(l_freq, key=l_freq.get), min(l_freq, key=l_freq.get)
    extr_diff = max(l_freq.values()) - min(l_freq.values())
    print(f"Most freq letter: {max_c}, least freq: {min_c}. Their diff is {extr_diff}")


