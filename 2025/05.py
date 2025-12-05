from collections.abc import Iterable

from aoc_utils import tuple2


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    ranges, items = inp.split("\n\n")
    ranges: list[tuple[int, int]] = [tuple2(map(int, line.split("-"))) for line in ranges.splitlines()]
    items: list[int] = list(map(int, items.splitlines()))

    yield 1, sum(1 for i in items if any(a <= i <= b for a, b in ranges))

    s, minn, maxx = 0, 0, -1
    for a, b in sorted(ranges):
        if a > maxx:
            s += maxx - minn + 1
            minn, maxx = a, b
        else:
            maxx = max(maxx, b)
    s += maxx - minn + 1
    yield 2, s


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
