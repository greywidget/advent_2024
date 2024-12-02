from puzzle02 import solve

puzzle_data = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]


def test_day02_puzzle01():
    assert solve(puzzle=1, puzzle_data=puzzle_data) == 2


def test_day02_puzzle01_solved():
    assert solve(puzzle=1) == 421


def test_day02_puzzle02():
    assert solve(puzzle=2, puzzle_data=puzzle_data) == 4


def test_day02_puzzle02_solved():
    assert solve(puzzle=2) == 476
