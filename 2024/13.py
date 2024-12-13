import re
from collections.abc import Iterable

import cpmpy as cp
from more_itertools import grouper
from tqdm import tqdm


def solve_part(inp: list[tuple[tuple[int, ...], ...]], offset: int) -> int:
    tokens = 0
    for a, b, prize in tqdm(inp):
        x, y = cp.intvar(0, 100 + offset), cp.intvar(0, 100 + offset)
        m = cp.Model(
            prize[0] + offset == a[0] * x + b[0] * y,
            prize[1] + offset == a[1] * x + b[1] * y,
        )
        if m.solve():
            tokens += x.value() * 3 + y.value()
    return tokens


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    inp = [tuple(map(tuple, grouper(map(int, x), 2))) for x in
           re.findall(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)", inp)]
    yield 1, solve_part(inp, 0)
    yield 2, solve_part(inp, 10000000000000)


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
