from functools import cache
from hashlib import md5

from aoc_utils import Vec
from aocd import get_data


def open_doors(salt, path):
    h = md5((salt + path).encode()).hexdigest()[:4]
    return [d for d, hd in zip(['U', 'D', 'L', 'R'], h) if hd in 'bcdef']


@cache
def path_to_coords(path):
    if path == '':
        return Vec(0, 0)
    return path_to_coords(path[:-1]) + {'U': Vec(0, -1), 'D': Vec(0, 1), 'L': Vec(-1, 0), 'R': Vec(1, 0)}[path[-1]]


def part1(inp):
    paths = {''}
    while paths:
        np = set()
        for p in paths:
            for d in open_doors(inp, p):
                x, y = path_to_coords(p+d)
                if (x, y) == (3, 3):
                    return p + d
                if 0 <= x <= 3 and 0 <= y <= 3:
                    np.add(p+d)
        paths = np


def part2(inp):
    paths = {''}
    longest = 0
    while paths:
        np = set()
        for p in paths:
            for d in open_doors(inp, p):
                x, y = path_to_coords(p+d)
                if (x, y) == (3, 3):
                    if len(p+d) > longest:
                        longest = len(p+d)
                elif 0 <= x <= 3 and 0 <= y <= 3:
                    np.add(p+d)
        paths = np
    return longest


if __name__ == '__main__':
    inp = get_data(day=17, year=2016)
    print(part1(inp))
    print(part2(inp))
