import re
from collections.abc import Iterable

from aocd_runner import aocd_run_solver


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    inp = [
        tuple(map(int, re.match(r"(\d+)x(\d+): (\d+) (\d+) (\d+) (\d+) (\d+) (\d+)", l).groups()))  # type: ignore[union-attr]
        for l in inp.rsplit("\n\n", maxsplit=1)[-1].splitlines()
    ]
    yield 1, sum(1 for x in inp if can_fit(x))


# This only works for the simple case with enough space for every 3x3 block.
# TODO at least also check lower bounds to error out on non-tivial cases
def can_fit(inp: tuple[int, ...]) -> bool:
    x, y, *a = inp
    x //= 3
    y //= 3
    return x * y >= sum(a)


if __name__ == "__main__":
    aocd_run_solver(solve)
