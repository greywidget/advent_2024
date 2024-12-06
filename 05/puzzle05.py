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


class Puzzle:
    def __init__(self, puzzle_data):
        self.rules = self._get_rules(puzzle_data[0])
        self._updates = puzzle_data[1]

    def _get_rules(self, rule_data):
        return [tuple(map(int, item.split("|"))) for item in rule_data]

    def _get_middle_page(self, update):
        pos = len(update) // 2
        for index, item in enumerate(update.keys()):
            if index == pos:
                return item

    def next_update(self):
        for item in self._updates:
            update = {int(value): index for index, value in enumerate(item.split(","))}
            yield update

    def apply_rules(self, update):
        for rule in self.rules:
            if all(item in update.keys() for item in rule):
                first, second = rule
                if update[first] > update[second]:
                    return False
        return True


def solve(puzzle=1, puzzle_data=puzzle_data):
    if puzzle == 1:
        puzzle = Puzzle(puzzle_data)
        middle_page_sum = 0
        for update in puzzle.next_update():
            if puzzle.apply_rules(update):
                middle_page_sum += puzzle._get_middle_page(update)

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
