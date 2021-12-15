import math
from collections import defaultdict
from itertools import product

from aoc_utils import Vec, dirs4
from aocd import get_data


def find_shortest_path(mapp):
    start = Vec(0, 0)
    goal = max(mapp, key=sum)

    def h(n):
        return (n - start).manhatten()

    openSet = {start}
    gScore = defaultdict(lambda: math.inf, {start: 0})
    fScore = defaultdict(lambda: math.inf, {start: h(start)})

    while openSet:
        current = min(openSet, key=fScore.get)
        if current == goal:
            return gScore[current]
        openSet.remove(current)
        for neighbor in (current + d for d in dirs4 if (current + d) in mapp):
            tentative_gScore = gScore[current] + mapp[neighbor]
            if tentative_gScore < gScore[neighbor]:
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + h(neighbor)
                if neighbor not in openSet:
                    openSet.add(neighbor)


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
