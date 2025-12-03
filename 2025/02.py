from collections.abc import Iterable

from aoc_utils import tuple2


def is_valid(x: int) -> bool:
    x = str(x)
    return x[: len(x) // 2] != x[len(x) // 2 :]


def is_valid2(x: int) -> bool:
    x = str(x)
    l = len(x)
    for i in range(1, l // 2 + 1):
        if l % i != 0:
            continue
        if all(x[:i] == x[i * j : i * (j + 1)] for j in range(1, l // i)):
            return False
    return True


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    inp: list[tuple[int, int]] = [tuple2(map(int, a.split("-"))) for a in inp.split(",")]
    yield 1, sum(i for a, b in inp for i in range(a, b + 1) if not is_valid(i))
    yield 2, sum(i for a, b in inp for i in range(a, b + 1) if not is_valid2(i))


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
