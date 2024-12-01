from collections import Counter
from pathlib import Path


def _get_ints(data: list[str]):
    return (int(data[0]), int(data[1]))


def part_one(list1, list2):
    print("\nPart One")
    print("=" * 8)
    data = zip(sorted(list1), sorted(list2))
    print(sum(abs(first - second) for first, second in data))


def part_two(list1, list2):
    print("\nPart Two")
    print("=" * 8)
    counter = Counter(list2)
    print(sum(item * counter.get(item, 0) for item in list1))
    print()


def main():
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

    part_one(list1, list2)
    part_two(list1, list2)


if __name__ == "__main__":
    main()
