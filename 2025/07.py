from collections import defaultdict
from collections.abc import Iterable

from aoc_utils import DOWN, LEFT, RIGHT, Vec, create_map


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    mapp = create_map(inp)
    tachyons = {p: 1 for p, v in mapp.items() if v == "S"}
    splits = 0
    while True:
        new_tachyons: dict[Vec, int] = defaultdict(int)
        for p, v in tachyons.items():
            if mapp.get(p + DOWN) == ".":
                new_tachyons[p + DOWN] += v
            elif mapp.get(p + DOWN) == "^":
                new_tachyons[p + DOWN + LEFT] += v
                new_tachyons[p + DOWN + RIGHT] += v
                splits += 1
        if new_tachyons:
            tachyons = new_tachyons
        else:
            break
    yield 1, splits
    yield 2, sum(tachyons.values())


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
