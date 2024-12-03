import re
from collections.abc import Iterable


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    part1 = lambda x: sum(int(a) * int(b) for a, b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", x))
    yield 1, part1(inp)
    yield 2, part1(" ".join(a.split("don't()")[0] for a in inp.split("do()")))


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
