# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from assertpy import assert_that
from statistics import median


def extract_codes_from_file(file_name: str) -> list[str]:
    with open(file_name, 'r') as data_file:
        return [c.strip() for c in data_file.readlines()]


def get_point_for_closing_char(c: str) -> int:
    points_dict = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    return points_dict.get(c, 0)


def p2_get_point_for_closing_char(c: str) -> int:
    points_dict = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    return points_dict.get(c, 0)


def is_corresponding(prev_c: str, current_c: str) -> bool:
    cor_dict = {
        '(': ')',
        '{': '}',
        '[': ']',
        '<': '>'
    }
    return current_c == cor_dict.get(prev_c)


def get_closing_for_opening(open_c: str) -> str:
    cor_dict = {
        '(': ')',
        '{': '}',
        '[': ']',
        '<': '>'
    }
    return cor_dict.get(open_c)


def get_total(list_codes: list[str]) -> int:
    total_score = 0
    for line in list_codes:
        expect = []
        for char in line:
            if char in ['{', '[', '<', '(']:
                expect.append(char)
            elif is_corresponding(expect[-1], char):
                expect.pop()
            else:
                total_score += get_point_for_closing_char(char)
                break
    return total_score


def p2_get_score_from_line(code_line: str) -> int:
    total_score = 0
    expect = []
    for char in code_line:
        if char in ['{', '[', '<', '(']:
            expect.append(char)
        elif is_corresponding(expect[-1], char):
            expect.pop()
        else:
            break
    else:
        for b_left in reversed(expect):
            total_score *= 5
            total_score += p2_get_point_for_closing_char(get_closing_for_opening(b_left))
    return total_score


def p2_get_total(list_codes: list[str]) -> int:
    all_scores = []
    for line in list_codes:
        if p2_get_score_from_line(line):
            all_scores.append(p2_get_score_from_line(line))

    return median(all_scores)


if __name__ == '__main__':
    # PART1 TEST
    nav_lines = extract_codes_from_file("data_test.txt")
    answer = get_total(nav_lines)
    assert_that(answer).is_equal_to(26397)

    # PART1 REAL
    nav_lines = extract_codes_from_file("data_real.txt")
    answer = get_total(nav_lines)
    assert_that(answer).is_not_equal_to(26397)
    print(answer)

    # PART2 TEST
    nav_lines = extract_codes_from_file("data_test.txt")
    assert_that(p2_get_total(['[({(<(())[]>[[{[]{<()<>>'])).is_equal_to(288957)
    assert_that(p2_get_total(['[(()[<>])]({[<{<<[]>>('])).is_equal_to(5566)
    assert_that(p2_get_total(['(((({<>}<{<{<>}{[]{[]{}'])).is_equal_to(1480781)
    total = p2_get_total(nav_lines)
    assert_that(total).is_equal_to(288957)

    # PART2 REAL
    nav_lines = extract_codes_from_file("data_real.txt")
    total = p2_get_total(nav_lines)
    assert_that(total).is_not_equal_to(288957)
    print(total)

