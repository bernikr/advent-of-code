from collections import Counter, defaultdict
from collections.abc import Iterable

from aoc_utils import Vec, dirs4


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    mapp = {Vec(x, y): int(c) for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l)}
    peaks = {p: {p} for p, c in mapp.items() if c == 9}
    trails = {p: 1 for p, c in mapp.items() if c == 9}
    for i in reversed(range(9)):
        new_peaks = defaultdict(set)
        new_trails = Counter()
        for p, peak in peaks.items():
            for d in dirs4:
                if mapp.get(p + d, 10) == i:
                    new_peaks[p + d] |= peak
                    new_trails[p + d] += trails[p]
        trails = new_trails
        peaks = new_peaks
    yield 1, sum(len(a) for a in peaks.values())
    yield 2, sum(trails.values())


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
