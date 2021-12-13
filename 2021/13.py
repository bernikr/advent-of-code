import re

from aoc_utils import ocr
from aocd import get_data


def fold(ins, coords):
    res = set()
    d, line = ins
    for x, y in coords:
        if d == 'x' and x > line:
            x = 2 * line - x
        elif d == 'y' and y > line:
            y = 2 * line - y
        res.add((x, y))
    return res


def part1(inp):
    coords, ins = inp
    return len(fold(ins[0], coords))


def part2(inp):
    coords, ins = inp
    for i in ins:
        coords = fold(i, coords)
    return ocr(coords)


if __name__ == '__main__':
    data = get_data(day=13, year=2021)
    coords, ins = data.split('\n\n')
    coords = [tuple(map(int, l.split(','))) for l in coords.splitlines()]
    ins = [(a, int(b)) for a, b in (re.match(r'^fold along ([xy])=(\d+)$', l).groups() for l in ins.splitlines())]
    inp = (coords, ins)
    print(part1(inp))
    print(part2(inp))
