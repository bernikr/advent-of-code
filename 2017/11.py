from itertools import accumulate

from aoc_utils import Vec

# Use Hexagonal Cube Coordinates: https://www.redblobgames.com/grids/hexagons/
dirs = {
    'n': Vec(0, -1, 1),
    'ne': Vec(1, -1, 0),
    'se': Vec(1, 0, -1),
    's': Vec(0, 1, -1),
    'sw': Vec(-1, 1, 0),
    'nw': Vec(-1, 0, 1)
}


def part1(inp):
    return max(map(abs, sum(map(dirs.get, inp), start=Vec(0, 0, 0))))


def part2(inp):
    return max(map(lambda x: max(abs(i) for i in x), accumulate(map(dirs.get, inp))))


def solve(inp, ispart1):
    inp = inp.split(',')
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
