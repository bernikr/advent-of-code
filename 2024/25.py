from collections.abc import Iterable
from itertools import combinations

from aoc_utils import create_map


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    inp = [{p for p, c in create_map(i).items() if c == "#"} for i in inp.split("\n\n")]
    yield 1, sum(a & b == set() for a, b in combinations(inp, 2))


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
