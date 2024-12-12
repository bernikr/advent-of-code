from collections import Counter, defaultdict
from collections.abc import Iterable

from aoc_utils import Vec, dirs4


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    mapp = {Vec(x, y): int(c) for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l)}
    peaks = defaultdict(set, {p: {p} for p, c in mapp.items() if c == 9})
    trails = Counter(p for p, c in mapp.items() if c == 9)
    for i in reversed(range(9)):
        for p, _ in filter(lambda x: x[1] == i + 1, mapp.items()):
            for d in dirs4:
                if mapp.get(p + d, 10) == i:
                    peaks[p + d] |= peaks[p]
                    trails[p + d] += trails[p]
    yield 1, sum(len(a) for p, a in peaks.items() if mapp[p] == 0)
    yield 2, sum(x for p, x in trails.items() if mapp[p] == 0)


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
