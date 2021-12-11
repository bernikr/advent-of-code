import re
from itertools import count

from aocd import get_data


def part1(inp):
    return next(i for i in count() if all((i + startpos + disknum) % size == 0 for disknum, size, startpos in inp))


def part2(inp):
    disks = inp.copy()
    disks.append((len(disks)+1, 11, 0))
    return next(i for i in count() if all((i + startpos + disknum) % size == 0 for disknum, size, startpos in disks))


if __name__ == '__main__':
    data = get_data(day=15, year=2016)
    inp = [
        tuple(map(int, re.match(r'Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).', l).groups()))
        for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
