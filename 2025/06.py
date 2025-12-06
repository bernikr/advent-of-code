import operator
from collections.abc import Iterable
from functools import reduce


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    operators: list[str] = inp.splitlines()[-1].split()
    numbers1: list[tuple[int, ...]] = list(zip(*(map(int, l.split()) for l in inp.splitlines()[:-1])))
    numbers2: list[tuple[int, ...]] = [
        tuple(map(int, p.splitlines()))
        for p in "\n".join("".join(map(str.strip, x)) for x in zip(*inp.splitlines()[:-1])).split("\n\n")
    ]
    for i, numbers in [(1, numbers1), (2, numbers2)]:
        yield (
            i,
            sum(
                reduce(operator.add if op == "+" else operator.mul, nums)
                for nums, op in zip(numbers, operators, strict=True)
            ),
        )


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
