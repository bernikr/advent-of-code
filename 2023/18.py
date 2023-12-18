import re
from itertools import accumulate, pairwise

from aoc_utils import UP, DOWN, LEFT, RIGHT, Vec


def solve(inp, part1):
    inp = [re.match(r"([UDLR]) (\d+) \(#([\da-f]{6})\)", l).groups() for l in inp.splitlines()]
    if part1:
        ins = [{"U": UP, "D": DOWN, "L": LEFT, "R": RIGHT}[a] * int(b) for a, b, _ in inp]
    else:
        ins = [[RIGHT, DOWN, LEFT, UP][int(a[-1])] * int(a[:-1], 16) for _, _, a in inp]
    return int((abs(sum(a[0] * b[1] - a[1] * b[0] for a, b in pairwise(accumulate(ins, initial=Vec(0, 0)))))
                + sum(abs(a) for a in ins)) / 2 + 1)  # see 2023 day 10


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
