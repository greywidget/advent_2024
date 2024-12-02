from puzzle01 import solve

list1 = [3, 4, 2, 1, 3, 3]
list2 = [4, 3, 5, 3, 9, 3]


def test_day01_puzzle01():
    assert solve(puzzle=1, list1=list1, list2=list2) == 11


def test_day01_puzzle01_solved():
    assert solve(puzzle=1) == 1189304
