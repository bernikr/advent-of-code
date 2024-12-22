from collections.abc import Collection, Iterable
from functools import cache


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    towels, patterns = inp.split("\n\n")
    towels = frozenset(towels.split(", "))
    arrangements = [check_pattern(p, towels) for p in patterns.splitlines()]
    yield 1, sum(map(bool, arrangements))
    yield 2, sum(arrangements)


@cache
def check_pattern(pattern: str, towels: Collection[str]) -> int:
    if len(pattern) == 0:
        return 1
    return sum(pattern.startswith(t) and check_pattern(pattern[len(t):], towels) for t in towels)


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
