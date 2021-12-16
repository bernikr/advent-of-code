import re
from collections import Counter

from aoc_utils import Vec
from aocd import get_data


def part1(inp):
    return min(((a.manhatten(), v.manhatten(), p.manhatten(), n) for n, (p, v, a) in enumerate(inp)))[3]


def move(p):
    pos, vel, acc = p
    vel += acc
    pos += vel
    return pos, vel, acc


def part2(inp):
    parts = inp
    for _ in range(100):
        collisions = [p for p, n in Counter(p for p, _, _ in parts).items() if n > 1]
        parts = [move(p) for p in parts if p[0] not in collisions]
    return len(parts)


if __name__ == '__main__':
    data = get_data(day=20, year=2017)
    inp = [tuple(map(lambda x: Vec(*map(int, x.split(','))),
                     re.match(r'^p=<([\d,-]+)>, v=<([\d,-]+)>, a=<([\d,-]+)>$', l).groups()))
           for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
