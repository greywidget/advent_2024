from pathlib import Path

WORD = "XMAS"


def _import_data():
    data = []

    data_file = Path(__file__).resolve().parent / "raw_data.txt"

    with open(data_file, "r", encoding="utf8") as f:
        line = f.readline().strip()
        while line:
            data.append(line)
            line = f.readline().strip()

    return data


puzzle_data = _import_data()


class Puzzle:
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def __init__(self, word, data):
        self.word = word
        self.word_len = len(word)
        self.data = data
        self.rows, self.cols = len(data), len(data[0])

    def _in_range(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols

    def _search(self, x, y, dx, dy):
        for i in range(self.word_len):
            pos_x, pos_y = x + dx * i, y + dy * i
            if (
                not self._in_range(pos_x, pos_y)
                or self.data[pos_x][pos_y] != self.word[i]
            ):
                return False
        return True

    def count_matches(self):
        match_count = 0

        for row in range(self.rows):
            for col in range(self.cols):
                for dx, dy in self.directions:
                    if self._search(row, col, dx, dy):
                        match_count += 1

        return match_count


class Puzzle2:
    def __init__(self, data):
        self.data = data
        self.rows, self.cols = len(data), len(data[0])

    def _search(self, x, y, m_or_s):
        other = "M" if m_or_s == "S" else "S"
        # Check left top to bottom right
        if self.data[x + 1][y + 1] == "A" and self.data[x + 2][y + 2] == other:
            if (
                self.data[x][y + 2] == "M"
                and self.data[x + 2][y] == "S"
                or self.data[x][y + 2] == "S"
                and self.data[x + 2][y] == "M"
            ):
                return True

        return False

    def count_matches(self):
        match_count = 0

        for row in range(self.rows - 2):
            for col in range(self.cols - 2):
                if (item := self.data[row][col]) in "MS":
                    if self._search(row, col, item):
                        match_count += 1

        return match_count


def solve(puzzle=1, puzzle_data=puzzle_data):
    if puzzle == 1:
        puzzle = Puzzle(WORD, puzzle_data)
        return puzzle.count_matches()
    elif puzzle == 2:
        puzzle = Puzzle2(puzzle_data)
        return puzzle.count_matches()


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
