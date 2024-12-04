from puzzle04 import solve


puzzle_data = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]


def test_day4_puzzle01():
    assert solve(puzzle=1, puzzle_data=puzzle_data) == 18


def test_day04_puzzle01_solved():
    assert solve(puzzle=1) == 2468


def test_day4_puzzle02():
    assert solve(puzzle=2, puzzle_data=puzzle_data) == 9


def test_day04_puzzle02_solved():
    assert solve(puzzle=2) == 1864
