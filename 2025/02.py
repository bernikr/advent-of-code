from collections.abc import Iterable
from itertools import chain, count

from more_itertools import unique

from aoc_utils import tuple2


def generate_invalid(minn: int, maxx: int, reps: int) -> Iterable[int]:
    min_str = str(minn)
    start = int(min_str[: len(min_str) // reps]) if len(min_str) >= reps else 0
    for i in count(start):
        x = int(str(i) * reps)
        if x < minn:
            continue
        if x > maxx:
            break
        yield x


def generate_all_invalid(minn: int, maxx: int) -> Iterable[int]:
    return unique(chain.from_iterable(generate_invalid(minn, maxx, i) for i in range(2, len(str(maxx)) + 1)))


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    inp: list[tuple[int, int]] = [tuple2(map(int, a.split("-"))) for a in inp.split(",")]
    yield 1, sum(i for a, b in inp for i in generate_invalid(a, b, 2))
    yield 2, sum(i for a, b in inp for i in generate_all_invalid(a, b))


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
