from pathlib import Path


def _get_ints(data: list[str]):
    return (int(data[0]), int(data[1]))


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

    data = zip(sorted(list1), sorted(list2))
    print(sum(abs(first - second) for first, second in data))


if __name__ == "__main__":
    main()
