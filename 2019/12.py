import operator
import re
from copy import deepcopy

from itertools import combinations, count
from math import lcm


def part1(a):
    pos = deepcopy(a)
    vel = [[0, 0, 0] for _ in a]

    for _ in range(1000):
        for a, b in combinations(range(len(pos)), 2):
            for i in range(3):
                if pos[a][i] > pos[b][i]:
                    vel[a][i] -= 1
                    vel[b][i] += 1
                elif pos[a][i] < pos[b][i]:
                    vel[a][i] += 1
                    vel[b][i] -= 1
        pos = [tuple(map(operator.add, p, v)) for p, v in zip(pos, vel)]

    return sum(sum(map(abs, p)) * sum(map(abs, v)) for p, v in zip(pos, vel))


def part2(a):
    pos = deepcopy(a)
    vel = [[0, 0, 0] for _ in a]

    start = deepcopy(pos)
    period = [None for _ in range(3)]
    for it in count(start=1):
        for a, b in combinations(range(len(pos)), 2):
            for i in range(3):
                if pos[a][i] > pos[b][i]:
                    vel[a][i] -= 1
                    vel[b][i] += 1
                elif pos[a][i] < pos[b][i]:
                    vel[a][i] += 1
                    vel[b][i] -= 1
        pos = [tuple(map(operator.add, p, v)) for p, v in zip(pos, vel)]
        for i in range(3):
            if period[i] is None and all(p[i] == s[i] for p, s in zip(pos, start)) and all(v[i] == 0 for v in vel):
                period[i] = it
        if all(period):
            break
    return lcm(*period)


def solve(inp, ispart1):
    inp = [tuple(map(int, re.match(r'^<x=(-?\d+), y=(-?\d+), z=(-?\d+)>$', l).groups())) for l in inp.splitlines()]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
