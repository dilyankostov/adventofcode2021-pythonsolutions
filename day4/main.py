# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from assertpy import assert_that
import math


def get_bingo_numbers_and_boards(file_name: str) -> (list[str], list[list[str]]):
    with open(file_name, 'r') as data_file:
        line1 = data_file.readline().strip().split(',')
        line1 = [n.strip() for n in line1]
        boards = []
        for line in data_file:
            if line == '\n':
                boards.append([])
            else:
                line_list = line.strip().split()
                boards[len(boards) - 1].append([n.strip() for n in line_list])
        print(boards)
    return line1, boards


def calc_score(bingo_winning_num: str, unused_board: list[list[str]]) -> int:
    unused_sum = 0
    for unused_line in unused_board:
        unused_sum += sum([int(n) for n in unused_line if n.isdigit()])
    return int(bingo_winning_num) * unused_sum


def do_bingo(bingo_numbers, bingo_boards):
    for bingo_num in bingo_numbers:
        for board in bingo_boards:
            for n, line in enumerate(board):
                board[n] = [num if num != bingo_num else '' for num in line]
            for i in range(len(board)):
                if all(num == '' for num in [n[i] for n in board]) or \
                        all(num == '' for num in [n for n in board[i]]):
                    return calc_score(bingo_num, board)


def do_loser_bingo(bingo_numbers, bingo_boards):
    num_boards = len(bingo_boards)
    for bingo_num in bingo_numbers:
        for board_n, board in enumerate(bingo_boards):
            for n, line in enumerate(board):
                board[n] = [num if num != bingo_num else '' for num in line]
            for i in range(len(board)):
                if all(num == '' for num in [n[i] for n in board]) or \
                        all(num == '' for num in [n for n in board[i]]):
                    if num_boards == 1:
                        return calc_score(bingo_num, board)
                    else:
                        num_boards -= 1
                        bingo_boards[board_n] = [list(map(lambda x: 'X', x)) for x in bingo_boards[board_n]]
                        break


if __name__ == '__main__':
    # PART1 TEST
    bingo_nums, boards_test = get_bingo_numbers_and_boards("data_test.txt")
    score = do_bingo(bingo_nums, boards_test)
    assert_that(score).is_equal_to(4512)

    # PART1 REAL
    bingo_nums, boards_real = get_bingo_numbers_and_boards("data_real.txt")
    score = do_bingo(bingo_nums, boards_real)
    assert_that(score).is_not_equal_to(4512)
    print(score)

    # PART2 TEST
    bingo_nums, boards_test = get_bingo_numbers_and_boards("data_test.txt")
    score = do_loser_bingo(bingo_nums, boards_test)
    assert_that(score).is_equal_to(1924)

    # PART2 REAL
    bingo_nums, boards_real = get_bingo_numbers_and_boards("data_real.txt")
    score = do_loser_bingo(bingo_nums, boards_real)
    assert_that(score).is_not_equal_to(1924)
    print(score)







