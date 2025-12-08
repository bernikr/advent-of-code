from collections.abc import Iterable
from typing import Any

from aocd_runner import NO_EXTRA, aocd_run_solver


def solve(inp: str, extra: dict[str, Any] = NO_EXTRA) -> Iterable[tuple[int, int | str]]:
    inp = inp.splitlines()
    print(inp)
    yield 1, ""


if __name__ == "__main__":
    aocd_run_solver(solve)
