import operator
import re
from collections.abc import Iterable
from functools import reduce

import cpmpy as cp  # type: ignore[import-untyped]

from aocd_runner import aocd_run_solver


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    machines = [parse_line(line) for line in inp.splitlines()]
    yield 1, solve_machines1(machines)
    yield 2, solve_machines2(machines)


def parse_line(line: str) -> tuple[list[bool], list[list[int]], list[int]]:
    res = re.match(r"^\[([\.#]+)\] ([\()\d, ]+) {([\d,]+)}$", line)
    if not res:
        msg = f"Could not parse line: {line}"
        raise ValueError(msg)
    a, b, c = res.groups()
    a = [x == "#" for x in a]
    b = [[int(x) for x in y.split(",")] for y in b.replace(")", "").replace("(", "").split(" ")]
    c = [int(x) for x in c.split(",")]
    return a, b, c


def solve_machines1(machines: list[tuple[list[bool], list[list[int]], list[int]]]) -> int:
    m = cp.Model()
    total = 0
    for state, buttons, _ in machines:
        b = cp.boolvar(shape=len(buttons))
        for i, s in enumerate(state):
            m.add(s == reduce(operator.xor, (b[j] for j, button in enumerate(buttons) if i in button)))
        total += sum(b)
    m.minimize(total)
    m.solve()
    return m.objective_value()  # type: ignore[no-any-return]


def solve_machines2(machines: list[tuple[list[bool], list[list[int]], list[int]]]) -> int:
    m = cp.Model()
    total = 0
    for _, buttons, joltages in machines:
        b = cp.intvar(shape=len(buttons), lb=0, ub=max(joltages))
        for i, jolt in enumerate(joltages):
            m.add(jolt == sum(b[j] for j, button in enumerate(buttons) if i in button))
        total += sum(b)
    m.minimize(total)
    m.solve()
    return m.objective_value()  # type: ignore[no-any-return]


if __name__ == "__main__":
    aocd_run_solver(solve)
