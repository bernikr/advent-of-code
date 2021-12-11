from itertools import count

from aoc_utils import dirs8, Vec
from aocd import get_data


def part1(inp):
    octos = inp.copy()
    res = 0
    for _ in range(100):
        for k in octos:
            octos[k] += 1
        flashed = set()
        while any(v > 9 and k not in flashed for k, v in octos.items()):
            o = next(k for k, v in octos.items() if v > 9 and k not in flashed)
            flashed.add(o)
            for d in dirs8:
                if (o + d) in octos:
                    octos[o + d] += 1
        for o in flashed:
            octos[o] = 0
        res += len(flashed)
    return res


def part2(inp):
    octos = inp.copy()
    for i in count():
        for k in octos:
            octos[k] += 1
        flashed = set()
        while any(v > 9 and k not in flashed for k, v in octos.items()):
            o = next(k for k, v in octos.items() if v > 9 and k not in flashed)
            flashed.add(o)
            for d in dirs8:
                if (o + d) in octos:
                    octos[o + d] += 1
        if len(flashed) == len(octos):
            return i + 1
        for o in flashed:
            octos[o] = 0


if __name__ == '__main__':
    data = get_data(day=11, year=2021)
    inp = {Vec(x, y): int(c) for y, l in enumerate(data.splitlines()) for x, c in enumerate(l)}
    print(part1(inp))
    print(part2(inp))
