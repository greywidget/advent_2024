from pathlib import Path


def _import_data():
    page_order = []
    page_updates = []
    target = page_order

    data_file = Path(__file__).resolve().parent / "raw_data.txt"

    with open(data_file, "r", encoding="utf8") as f:
        line = f.readline()
        while line:
            if line == "\n":
                target = page_updates
            else:
                target.append(line.strip())

            line = f.readline()

    return page_order, page_updates


puzzle_data = _import_data()


def next_rule(rule_data):
    for item in rule_data:
        first, second = item.split("|")
        yield int(first), int(second)


def next_update(update_data):
    for item in update_data:
        update = {int(value): index for index, value in enumerate(item.split(","))}
        yield update


def middle_page(update):
    pos = len(update) // 2
    for index, item in enumerate(update.keys()):
        if index == pos:
            return item


def correctly_ordered(update, rule_data):
    for rule in next_rule(rule_data):
        if all(item in update.keys() for item in rule):
            first, second = rule
            if update[first] > update[second]:
                return False
    return True


def solve(puzzle=1, puzzle_data=puzzle_data):
    rule_data, update_data = puzzle_data
    if puzzle == 1:
        middle_page_sum = 0
        for update in next_update(update_data):
            if correctly_ordered(update, rule_data):
                middle_page_sum += middle_page(update)

    return middle_page_sum


def main():
    print("\nPart One")
    print("=" * 8)
    print(solve(puzzle=1))

    # print("\nPart Two")
    # print("=" * 8)
    # print(solve(puzzle=2))
    # print()


if __name__ == "__main__":
    main()
