from collections.abc import Iterable
from itertools import product

from aoc_utils import Vec, dirs8


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    mapp = {Vec(x, y): c for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l)}
    yield 1, sum("".join(mapp.get(pos + d * i, "") for i in range(4)) == "XMAS"
                 for pos, d in product(mapp.keys(), dirs8))
    yield 2, sum((mapp.get(pos) == "A" and
                  {mapp.get(pos + d) for d in [Vec(-1, -1), Vec(1, 1)]} == set("MS") and
                  {mapp.get(pos + d) for d in [Vec(-1, 1), Vec(1, -1)]} == set("MS"))
                 for pos in mapp)


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
