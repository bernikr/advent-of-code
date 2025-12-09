from collections.abc import Iterable
from heapq import heapify, heappop
from itertools import combinations

from shapely import Polygon, box, within

from aoc_utils import Vec
from aocd_runner import aocd_run_solver


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    inp: list[Vec] = [Vec(*map(int, line.split(","))) for line in inp.splitlines()]
    candidates = [(-(abs(a.x - b.x) + 1) * (abs(a.y - b.y) + 1), a, b) for a, b in combinations(inp, 2)]
    heapify(candidates)
    yield 1, -candidates[0][0]
    polygon = Polygon(inp)
    while True:
        s, a, b = heappop(candidates)
        if within(box(a.x, a.y, b.x, b.y), polygon):
            yield 2, -s
            return


if __name__ == "__main__":
    aocd_run_solver(solve)
