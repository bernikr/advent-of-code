from collections.abc import Iterable
from itertools import combinations

from aoc_utils import Vec
from aocd_runner import aocd_run_solver


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    inp = [Vec(*map(int, line.split(","))) for line in inp.splitlines()]
    yield 1, max((abs(a.x - b.x) + 1) * (abs(a.y - b.y) + 1) for a, b in combinations(inp, 2))


if __name__ == "__main__":
    aocd_run_solver(solve)
