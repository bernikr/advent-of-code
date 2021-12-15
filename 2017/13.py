from itertools import count

from aocd import get_data


def part1(inp):
    sev = 0
    for l, c in inp.items():
        if l % ((c - 1) * 2) == 0:
            sev += l * c
    return sev


def is_caught(inp, delay):
    for l, c in inp.items():
        if (l + delay) % ((c - 1) * 2) == 0:
            return True
    return False


def part2(inp):
    for i in count():
        if not is_caught(inp, i):
            return i


if __name__ == '__main__':
    data = get_data(day=13, year=2017)
    inp = {int(a): int(b) for a, b in (l.split(': ') for l in data.splitlines())}
    print(part1(inp))
    print(part2(inp))
