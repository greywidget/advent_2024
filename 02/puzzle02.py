from operator import gt, lt
from pathlib import Path


def _import_data():
    data = []

    data_file = Path(__file__).resolve().parent / "raw_data.txt"

    with open(data_file, "r", encoding="utf8") as f:
        line = f.readline()
        while line:
            report = line.strip().split()
            data.append(report)
            line = f.readline()
    return data


puzzle_data = _import_data()


def _report_safe(report):
    if len(report) < 2:
        return True

    if (first := int(report[0])) > int(report[1]):
        oper = lt
        prev = first + 1
    else:
        oper = gt
        prev = first - 1

    for item in report:
        int_item = int(item)
        if oper(prev, int_item) or not (0 < abs(prev - int_item) < 4):
            return False
        prev = int_item

    return True


def part_one(puzzle_data):
    safe_count = 0
    for report in puzzle_data:
        if _report_safe(report):
            safe_count += 1

    return safe_count


# def part_two(list1, list2):
#     counter = Counter(list2)
#     return sum(item * counter.get(item, 0) for item in list1)
#     print()


def solve(puzzle=1, puzzle_data=puzzle_data):
    if puzzle == 1:
        return part_one(puzzle_data)
    # elif puzzle == 2:
    #     return part_two(puzzle_data)


def main():
    print("\nPart One")
    print("=" * 8)
    print(part_one(puzzle_data=puzzle_data))

    # print("\nPart Two")
    # print("=" * 8)
    # print()


if __name__ == "__main__":
    main()
