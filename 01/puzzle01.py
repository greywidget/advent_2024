from collections import Counter
from pathlib import Path


def _get_ints(data: list[str]):
    return (int(data[0]), int(data[1]))


def _import_data():
    list1 = []
    list2 = []

    data_file = Path(__file__).resolve().parent / "raw_data.txt"

    with open(data_file, "r", encoding="utf8") as f:
        line = f.readline()
        while line:
            first, second = _get_ints(line.strip().split())
            list1.append(first)
            list2.append(second)
            line = f.readline()
    return (list1, list2)


left, right = _import_data()


def part_one(list1, list2):
    data = zip(sorted(list1), sorted(list2))
    return sum(abs(first - second) for first, second in data)


def part_two(list1, list2):
    counter = Counter(list2)
    return sum(item * counter.get(item, 0) for item in list1)
    print()


def solve(puzzle=1, list1=left, list2=right):
    if puzzle == 1:
        return part_one(list1, list2)
    elif puzzle == 2:
        return part_two(list1, list2)


def main():
    print("\nPart One")
    print("=" * 8)
    print(part_one(list1=left, list2=right))

    print("\nPart Two")
    print("=" * 8)

    print(part_two(list1=left, list2=right))
    print()


if __name__ == "__main__":
    main()
