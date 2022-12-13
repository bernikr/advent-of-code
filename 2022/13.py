import functools
import json
from itertools import zip_longest

from aoc_utils import sign
from aocd import data, submit, AocdError


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return sign(a - b)
    elif isinstance(a, list) and isinstance(b, list):
        for x, y in zip_longest(a, b):
            if x is None:
                return -1
            if y is None:
                return 1
            if (res := compare(x, y)) != 0:
                return res
        return 0
    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)


def solve(inp, part1):
    if part1:
        inp = [tuple(json.loads(l) for l in t.splitlines()) for t in inp.split('\n\n')]
        return sum(i + 1 for i, (a, b) in enumerate(inp) if compare(a, b) == -1)
    else:
        packets = [json.loads(l) for l in inp.splitlines() if l != '']
        packets.append([[2]])
        packets.append([[6]])
        packets = sorted(packets, key=functools.cmp_to_key(compare))
        return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


if __name__ == '__main__':
    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
