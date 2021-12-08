# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from assertpy import assert_that


def extract_codes_from_file(file_name: str) -> list[tuple[list[str], list[str]]]:
    with open(file_name, 'r') as data_file:
        data = []
        for line in data_file:
            data_in, data_out = line.strip().split(" | ")
            data.append((data_in.split(), data_out.split()))

    return data


def count_unique_len_words(list_of_sentences: list[tuple[list[str], list[str]]], unique_lens: list[int]) -> int:
    unique_total = 0
    for sentence in list_of_sentences:
        for word in sentence[1]:
            if len(word) in unique_lens:
                unique_total += 1
    return unique_total


def find_corresponding_int(code_words: list[str]) -> list[set[str]]:
    digits = [set()] * 10
    digits[1] = next(set(cw_) for cw_ in code_words if len(cw_) == 2)
    digits[4] = next(set(cw_) for cw_ in code_words if len(cw_) == 4)
    digits[7] = next(set(cw_) for cw_ in code_words if len(cw_) == 3)
    digits[8] = next(set(cw_) for cw_ in code_words if len(cw_) == 7)

    five_lens = (set(cw_) for cw_ in code_words if len(cw_) == 5)
    for five_len in five_lens:
        if digits[1].issubset(five_len):
            digits[3] = five_len
        elif len(digits[4] & five_len) == 3:
            digits[5] = five_len
        else:
            digits[2] = five_len

    six_lens = (set(cw_) for cw_ in code_words if len(cw_) == 6)
    for six_len in six_lens:
        if len(six_len & digits[4]) == 4:
            digits[9] = six_len
        elif len(six_len & digits[5]) == 5:
            digits[6] = six_len
        else:
            digits[0] = six_len
    return digits


def calc_output_from_solution_map(outputs: list[str], solution_matrix: list[set[str]]) -> int:
    value = 0
    for out in outputs:
        value = value * 10 + solution_matrix.index(set(out))
    return value


if __name__ == '__main__':
    # PART1 TEST
    codes = extract_codes_from_file("data_test.txt")
    weird_words_n = count_unique_len_words(codes, [2, 3, 4, 7])
    assert_that(weird_words_n).is_equal_to(26)

    # PART1 REAL
    codes = extract_codes_from_file("data_real.txt")
    weird_words_n = count_unique_len_words(codes, [2, 3, 4, 7])
    assert_that(weird_words_n).is_not_equal_to(26)
    print(weird_words_n)

    # PART2 TEST
    codes = extract_codes_from_file("data_test.txt")
    total = 0
    for code in codes:
        map_set = find_corresponding_int(code[0])
        total += calc_output_from_solution_map(code[1], map_set)
    assert_that(total).is_equal_to(61229)

    # PART1 REAL
    codes = extract_codes_from_file("data_real.txt")
    total = 0
    for code in codes:
        map_set = find_corresponding_int(code[0])
        total += calc_output_from_solution_map(code[1], map_set)
    assert_that(total).is_not_equal_to(61229)
    print(total)

    # dict_n = {
    #     0: ["a", "b", "c", "d", "e", "g"],
    #     1: ["c", "f"],
    #     2: ["a", "c", "d", "e", "g"],
    #     3: ["a", "c", "d", "f", "g"],
    #     4: ["b", "c", "d", "f"],
    #     5: ["a", "b", "d", "f", "g"],
    #     6: ["a", "b", "d", "e", "f", "g"],
    #     7: ["a", "c", "f"],
    #     8: ["a", "b", "c", "d", "e", "f", "g"],
    #     9: ["a", "b", "c", "d", "f", "g"],
    # }
    # dict_by_len = {
    #     2: [["c", "f"]],
    #     3: [["a", "c", "f"]],
    #     4: [["b", "c", "d", "f"]],
    #     6: [["a", "b", "c", "d", "e", "g"],["a", "b", "d", "e", "f", "g"],["a", "b", "c", "d", "f", "g"]],
    #     5: [["a", "c", "d", "e", "g"],["a", "c", "d", "f", "g"],["a", "b", "d", "f", "g"]],
    #     7: [["a", "b", "c", "d", "e", "f", "g"]]
    # }
    # all_letters = ["a", "b", "c", "d", "e", "f", "g"]







