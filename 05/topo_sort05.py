from collections import defaultdict, deque
from pathlib import Path

from rich import print


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


def generate_graph(pages, rules) -> dict:
    graph = defaultdict(list)
    for rule in rules:
        if all(page in pages for page in rule):
            first, second = rule
            graph[first].append(second)

    for page in pages:
        if page not in graph:
            graph[page] = []

    return graph


def middle_page(update):
    pos = len(update) // 2
    for index, item in enumerate(update):
        if index == pos:
            return item


def topological_sort(graph):
    # Track visited nodes
    visited = set()
    # Use a deque to store the sorted order (acts like a stack)
    order = deque()

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)
        # Add the node to the front of the deque after visiting neighbors
        order.appendleft(node)

    # Visit all nodes in the graph
    for node in graph:
        if node not in visited:
            dfs(node)

    return list(order)


def solve(puzzle=1, puzzle_data=puzzle_data):
    rule_data, update_data = puzzle_data

    middle_page_sum = 0

    rules = [
        (int(first), int(second))
        for first, second in (item.split("|") for item in rule_data)
    ]
    for index, update in enumerate(update_data):
        pages = [int(page) for page in update.split(",")]
        graph = generate_graph(pages, rules)
        list = topological_sort(graph)
        if puzzle == 1 and list == pages:
            middle_page_sum += middle_page(pages)
        elif puzzle == 2 and list != pages:
            middle_page_sum += middle_page(list)

    return middle_page_sum


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
