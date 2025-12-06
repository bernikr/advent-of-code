import operator
from collections.abc import Iterable
from functools import reduce


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    inp1 = [l.split() for l in inp.splitlines()]
    numbers: list[tuple[int, ...]] = list(zip(*(list(map(int, l)) for l in inp1[:-1])))
    operators: list[str] = inp1[-1]
    yield (
        1,
        sum(
            reduce(operator.add if op == "+" else operator.mul, nums)
            for nums, op in zip(numbers, operators, strict=True)
        ),
    )
    new_inp = [
        list(map(int, p.splitlines()))
        for p in "\n".join("".join(map(str.strip, x)) for x in zip(*inp.splitlines()[:-1])).split("\n\n")
    ]
    yield (
        2,
        sum(
            reduce(operator.add if op == "+" else operator.mul, nums)
            for nums, op in zip(new_inp, operators, strict=True)
        ),
    )


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
