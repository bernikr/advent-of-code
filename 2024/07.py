import operator
from collections.abc import Callable, Iterable, Sequence
from functools import reduce
from itertools import product

from tqdm import tqdm


def is_valid(l: Sequence[int], operators: Iterable[Callable[[int, int], int]]) -> bool:
    return any(l[0] == reduce(lambda x, y: y[1](x, y[0]), zip(l[2:], ops), l[1])
               for ops in product(operators, repeat=len(l) - 2))


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    inp = [list(map(int, l.replace(":", "").split())) for l in inp.splitlines()]
    ans1, ans2 = 0, 0
    for l in tqdm(inp):
        if is_valid(l, [operator.add, operator.mul]):
            ans1 += l[0]
        elif is_valid(l, [operator.add, operator.mul, lambda x, y: y + x * 10 ** len(str(y))]):
            ans2 += l[0]
    yield 1, ans1
    yield 2, ans1 + ans2


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
