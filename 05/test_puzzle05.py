from puzzle05 import solve


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


def test_day05_puzzle01_solved():
    assert solve(puzzle=1) == 6951


# def test_day4_puzzle02():
#     assert solve(puzzle=2, puzzle_data=puzzle_data) == 9


# def test_day04_puzzle02_solved():
#     assert solve(puzzle=2) == 1864

if __name__ == "__main__":
    test_day5_puzzle01()
