import math
from collections import defaultdict
from itertools import product
from queue import PriorityQueue

from aoc_utils import Vec, dirs4
from aocd import get_data


def find_shortest_path(mapp):
    start = Vec(0, 0)
    goal = max(mapp, key=sum)

    open_set = PriorityQueue()
    open_set.put((0, start))
    g_score = defaultdict(lambda: math.inf, {start: 0})

    while open_set:
        _, current = open_set.get()
        if current == goal:
            return g_score[current]
        for neighbor in (current + d for d in dirs4 if (current + d) in mapp):
            tentative_g_score = g_score[current] + mapp[neighbor]
            if tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + (neighbor - start).manhatten()
                open_set.put((f_score, neighbor))


def part1(inp):
    return find_shortest_path(inp)


def part2(inp):
    mapp = {}
    lx, ly = max(x for x, _ in inp) + 1, max(y for _, y in inp) + 1
    for (x, y), v in inp.items():
        for a, b in product(range(5), repeat=2):
            nv = (v + a + b) % 9
            mapp[Vec(x + a * lx, y + b * ly)] = 9 if nv == 0 else nv
    return find_shortest_path(mapp)


if __name__ == '__main__':
    data = get_data(day=15, year=2021)
    inp = {Vec(x, y): int(v) for y, l in enumerate(data.splitlines()) for x, v in enumerate(l)}
    print(part1(inp))
    print(part2(inp))
