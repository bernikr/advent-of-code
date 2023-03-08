import re
from dataclasses import dataclass
from operator import attrgetter

from aoc_utils import Vec


@dataclass
class Bot:
    pos: Vec
    r: int


def solve(inp, part1):
    exp = re.compile(r"-?\d+")
    bots = [Bot(Vec(x, y, z), r) for x, y, z, r in (map(int, exp.findall(l)) for l in inp.splitlines())]
    if part1:
        most_range = max(bots, key=attrgetter("r"))
        return sum(1 for b in bots if (most_range.pos-b.pos).manhatten() <= most_range.r)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
