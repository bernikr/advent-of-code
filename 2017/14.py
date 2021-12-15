from functools import cache

from aoc_utils import CircularList, Vec, dirs4
from aocd import get_data


@cache
def knothash(s):
    s = [ord(x) for x in s] + [17, 31, 73, 47, 23]
    l = CircularList(list(range(256)))
    pos, skip = 0, 0
    for _ in range(64):
        for length in s:
            l[pos:pos + length] = l[pos + length - 1:pos - 1:-1]
            pos += length + skip
            skip += 1
    dense = [0 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            dense[i] ^= l[i * 16 + j]
    return ''.join(format(x, '08b') for x in dense)


def part1(inp):
    return sum(sum(int(c) for c in knothash(f'{inp}-{i}')) for i in range(128))


def part2(inp):
    mapp = {Vec(x, y) for y in range(128) for x, c in enumerate(knothash(f'{inp}-{y}')) if c == '1'}
    regions = 0
    while mapp:
        regions += 1
        boundary = {mapp.pop()}
        while boundary:
            current = boundary.pop()
            for d in dirs4:
                if d + current in mapp:
                    mapp.remove(d + current)
                    boundary.add(d + current)
    return regions


if __name__ == '__main__':
    data = get_data(day=14, year=2017)
    inp = data
    print(part1(inp))
    print(part2(inp))
