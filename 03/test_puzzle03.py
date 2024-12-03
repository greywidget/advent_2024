from puzzle03 import solve


def test_day3_puzzle01():
    puzzle_data = (
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    )
    assert solve(puzzle=1, puzzle_data=puzzle_data) == 161


def test_day03_puzzle01_solved():
    assert solve(puzzle=1) == 183669043


def test_day03_puzzle02():
    puzzle_data = (
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )
    assert solve(puzzle=2, puzzle_data=puzzle_data) == 48


def test_day03_puzzle02_solved():
    assert solve(puzzle=2) == 59097164
