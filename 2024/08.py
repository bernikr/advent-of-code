import math
from collections import defaultdict
from collections.abc import Iterable
from itertools import product

from aoc_utils import create_map


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    mapp = create_map(inp)
    antennas = defaultdict(set)
    for p, c in mapp.items():
        if c != ".":
            antennas[c].add(p)
    antinodes1 = set()
    antinodes2 = set()
    for ps in antennas.values():
        for p1, p2 in product(ps, ps):
            if p1 != p2:
                antinodes1.add(p1 * 2 - p2)

                step = p2 - p1
                step /= math.gcd(*step)
                pos = p1
                while pos in mapp:
                    antinodes2.add(pos)
                    pos += step

    yield 1, len(antinodes1 & set(mapp))
    yield 2, len(antinodes2)


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
