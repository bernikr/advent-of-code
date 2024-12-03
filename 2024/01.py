from collections import Counter
from typing import Iterable


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    inp = tuple(zip(*(map(int, l.split("   ")) for l in inp.splitlines())))
    yield 1, sum(abs(a - b) for a, b in zip(*map(sorted, inp)))
    yield 2, sum(Counter(inp[1])[i] * i for i in inp[0])


if __name__ == "__main__":
    from aocd import data, submit, AocdError

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
