from collections.abc import Iterable

from aoc_utils import tuple2


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    ranges, items = inp.split("\n\n")
    ranges: list[tuple[int, int]] = [tuple2(map(int, line.split("-"))) for line in ranges.splitlines()]
    items: list[int] = list(map(int, items.splitlines()))

    yield 1, sum(1 for i in items if any(a <= i <= b for a, b in ranges))

    s, minn, maxx = 0, 0, -1  # max set to -1 to prevent adding initial 0
    for a, b in sorted(ranges):  # intervals sorted by start
        if a > maxx:  # if next interval does not overlap with current
            s += maxx - minn + 1  # add length of current interval
            minn, maxx = a, b  # start new interval
        else:  # if next interval overlaps with current
            maxx = max(maxx, b)  # extend current interval if needed
    s += maxx - minn + 1  # add last interval
    yield 2, s


if __name__ == "__main__":
    from aocd_runner import aocd_run_solver

    aocd_run_solver(solve)
