from cProfile import Profile

from puzzle05 import solve
from topo_sort05 import solve as better_solve

"""
There isn't that much difference between my original (puzzle05.py)
and the topological sort version (topo_sort5.py) for the simple test
data. But for the main test data the topo_sort is much improved.
"""

page_order = [
    "47|53",
    "97|13",
    "97|61",
    "97|47",
    "75|29",
    "61|13",
    "75|53",
    "29|13",
    "97|29",
    "53|29",
    "61|53",
    "97|53",
    "61|29",
    "47|13",
    "75|47",
    "97|75",
    "47|61",
    "75|61",
    "47|29",
    "75|13",
    "53|13",
]

page_updates = [
    "75,47,61,53,29",
    "97,61,53,29,13",
    "75,29,13",
    "75,97,47,61,53",
    "61,13,29",
    "97,13,75,29,47",
]

puzzle_data = page_order, page_updates


def test_day5_puzzle01():
    assert solve(puzzle=1, puzzle_data=puzzle_data) == 143


def test_day5_puzzle01_solved():
    assert solve(puzzle=1) == 6951


def test_day5_puzzle02():
    assert solve(puzzle=2, puzzle_data=puzzle_data) == 123


def test_day5_puzzle02_solved():
    assert solve(puzzle=2) == 4121


def test_improved_day5_puzzle01():
    assert better_solve(puzzle=1, puzzle_data=puzzle_data) == 143


def test_improved_day5_puzzle01_solved():
    assert better_solve(puzzle=1) == 6951


def test_improved_day5_puzzle02():
    assert better_solve(puzzle=2, puzzle_data=puzzle_data) == 123


def test_improved_day5_puzzle02_solved():
    assert better_solve(puzzle=2) == 4121


def main():
    profiler = Profile()
    profiler.runcall(test_improved_day5_puzzle02_solved)
    breakpoint()


if __name__ == "__main__":
    main()
