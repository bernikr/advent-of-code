from collections.abc import Iterable
from itertools import count

from aoc_utils import create_map, dirs8


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    mapp = {p for p, c in create_map(inp).items() if c == "@"}
    removed = 0
    for i in count():
        removable = {p for p in mapp if sum(1 for d in dirs8 if p + d in mapp) < 4}
        if i == 0:
            yield 1, len(removable)
        if not removable:
            yield 2, removed
            return
        mapp -= removable
        removed += len(removable)


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
