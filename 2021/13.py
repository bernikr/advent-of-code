import re

from aoc_utils import ocr


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


def solve(inp, ispart1):
    coords, ins = inp.split('\n\n')
    coords = [tuple(map(int, l.split(','))) for l in coords.splitlines()]
    ins = [(a, int(b)) for a, b in (re.match(r'^fold along ([xy])=(\d+)$', l).groups() for l in ins.splitlines())]
    inp = (coords, ins)
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
