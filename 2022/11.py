import operator
import re
from dataclasses import dataclass
from functools import reduce
from typing import Callable

from aocd import data, submit, AocdError

exp = r"Monkey \d:\n" \
      r"  Starting items: ([0-9, ]+)\n" \
      r"  Operation: new = (.+)\n" \
      r"  Test: divisible by (\d+)\n" \
      r"    If true: throw to monkey (\d)\n" \
      r"    If false: throw to monkey (\d)"


@dataclass
class Monkey:
    items: list[int]
    op: Callable[[int], int]
    divisor: int
    true_target: int
    false_target: int
    inspection_count: int = 0


def solve(inp, part1):
    monkeys = [Monkey(list(map(int, l.split(', '))), eval(f"lambda old: {op}"), int(div), int(tt), int(ft))
               for l, op, div, tt, ft in re.findall(exp, inp)]
    mod = reduce(operator.mul, (m.divisor for m in monkeys))
    for _ in range(20 if part1 else 10000):
        for i in range(len(monkeys)):
            for item in monkeys[i].items:
                monkeys[i].inspection_count += 1
                item = monkeys[i].op(item)
                if part1:
                    item = item // 3
                else:
                    item = item % mod
                if item % monkeys[i].divisor == 0:
                    monkeys[monkeys[i].true_target].items.append(item)
                else:
                    monkeys[monkeys[i].false_target].items.append(item)
            monkeys[i].items = []
    ins_counts = list(sorted(m.inspection_count for m in monkeys))
    return ins_counts[-1] * ins_counts[-2]


if __name__ == '__main__':
    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
