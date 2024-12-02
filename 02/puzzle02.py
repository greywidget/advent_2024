from copy import copy
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


def process(puzzle_data, dampen=False):
    safe_count = 0
    for report in puzzle_data:
        if _report_safe(report):
            safe_count += 1
        elif dampen:
            levels = len(report)
            for level in range(levels):
                temp_report = copy(report)
                temp_report.pop(level)
                if _report_safe(temp_report):
                    safe_count += 1
                    break

    return safe_count


def solve(puzzle=1, puzzle_data=puzzle_data):
    if puzzle == 1:
        return process(puzzle_data)
    elif puzzle == 2:
        return process(puzzle_data, dampen=True)


def main():
    print("\nPart One")
    print("=" * 8)
    print(solve(puzzle=1))

    print("\nPart Two")
    print("=" * 8)
    print(solve(puzzle=2))
    print()


if __name__ == "__main__":
    main()
