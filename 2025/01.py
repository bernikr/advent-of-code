from collections.abc import Iterable
from itertools import accumulate, chain


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    inp: list[int] = [int(l[1:]) * (-1 if l[0] == "L" else 1) for l in inp.splitlines()]
    yield 1, sum(1 if x % 100 == 0 else 0 for x in accumulate(inp, initial=50))
    inp = list(chain.from_iterable([x // abs(x)] * abs(x) for x in inp))
    yield 2, sum(1 if x % 100 == 0 else 0 for x in accumulate(inp, initial=50))


if __name__ == "__main__":
    from aocd_runner import aocd_run_solver

    aocd_run_solver(solve)
