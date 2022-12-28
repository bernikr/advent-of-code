import collections
import re


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


def solve(inp, ispart1):
    inp = [re.match(r"^([\w-]+)-(\d+)\[(\w+)\]$", l).groups() for l in inp.splitlines()]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
