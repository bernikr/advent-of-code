from collections.abc import Iterable
from itertools import pairwise


def is_safe(seq: Iterable[int]) -> bool:
    diff = [a - b for a, b in pairwise(seq)]
    return ((all(d > 0 for d in diff) or all(d < 0 for d in diff))
            and all(1 <= abs(d) <= 3 for d in diff))


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    inp = [tuple(map(int, l.split())) for l in inp.splitlines()]
    yield 1, sum(is_safe(l) for l in inp)
    yield 2, sum(any(is_safe(l[:i] + l[i + 1:]) for i in range(len(l) + 1)) for l in inp)


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
