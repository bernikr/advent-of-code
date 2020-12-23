import collections
import re

from aocd import get_data


def is_real(r):
    c = collections.Counter(r[0])
    c['-'] = 0
    return ''.join(map(lambda x: x[0], sorted(c.items(), key=lambda x: (-x[1], x[0]))[:5])) == r[2]


def part1(a):
    return sum(int(x[1]) for x in a if is_real(x))


def decrypt(r):
    return ''.join(' ' if c == '-' else chr((ord(c) - ord('a') + int(r[1])) % (ord('z') - ord('a') + 1) + ord('a'))
                   for c in r[0])


def part2(a):
    return next(x[1] for x in a if is_real(x) and decrypt(x) == 'northpole object storage')


if __name__ == '__main__':
    data = get_data(day=4, year=2016)
    inp = [re.match(r"^([\w-]+)-(\d+)\[(\w+)\]$", l).groups() for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
