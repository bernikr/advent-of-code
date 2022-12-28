import re
from itertools import count


def part1(inp):
    return next(i for i in count() if all((i + startpos + disknum) % size == 0 for disknum, size, startpos in inp))


def part2(inp):
    disks = inp.copy()
    disks.append((len(disks) + 1, 11, 0))
    return next(i for i in count() if all((i + startpos + disknum) % size == 0 for disknum, size, startpos in disks))


def solve(inp, ispart1):
    inp = [
        tuple(map(int, re.match(r'Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).', l).groups()))
        for l in inp.splitlines()]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
