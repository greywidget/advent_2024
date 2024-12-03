import re
from pathlib import Path

RE_WORD = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

"""
In the regular expression below, there are two main parts:

- (do\(\)|don't\(\)) matches either the string `do()` or the string `don't`
   This is Group(0)

- mul\((\d{1,3}),(\d{1,3})\) matches `mul(x,y)` where x and y are integers
  of 1 to 3 digits. This is Group(1)

  within the second part there are two sub parts:
  - (\d{1,3}) captures the first digit, this is Group(2)
  - (\d{1,3}) captures the first digit, this is Group(3)

Essentially at the top level we get a "do", a "don't" or a "mul"

"""

RE_WORD2 = re.compile(r"(do\(\)|don't\(\))|mul\((\d{1,3}),(\d{1,3})\)")


def _import_data():
    data = []

    data_file = Path(__file__).resolve().parent / "raw_data.txt"

    with open(data_file, "r", encoding="utf8") as f:
        data = f.read()

    return data


puzzle_data = _import_data()


def tokenize(puzzle_data, re_word=RE_WORD):
    for match in re_word.finditer(puzzle_data):
        yield (match.group(1), match.group(2))


def tokenize2(puzzle_data, re_word=RE_WORD2):
    enabled = True  # Matches start as enabled

    for match in re_word.finditer(puzzle_data):
        if match.group(1):  # Found "do()" or "don't()"
            if match.group(1) == "don't()":
                enabled = False
            elif match.group(1) == "do()":
                enabled = True
        elif (
            enabled and match.group(2) and match.group(3)
        ):  # Found "mul(x, y)" while enabled
            yield (match.group(2), match.group(3))


def solve(puzzle=1, puzzle_data=puzzle_data):
    if puzzle == 1:
        return sum(int(first) * int(second) for first, second in tokenize(puzzle_data))
    elif puzzle == 2:
        return sum(int(first) * int(second) for first, second in tokenize2(puzzle_data))


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
