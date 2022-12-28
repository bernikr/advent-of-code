import re
from itertools import count


def do_dance(dance, l):
    for ins in dance:
        match ins:
            case ('s', a, None):
                l = l[-a:] + l[:-a]
            case ('x', a, b):
                l[a], l[b] = l[b], l[a]
            case ('p', a, b):
                l = [a if c == b else b if c == a else c for c in l]
            case x:
                raise NotImplementedError(x)
    return l


def part1(inp):
    return ''.join(do_dance(inp, [chr(ord('a') + i) for i in range(16)]))


def part2(inp):
    cyclelen = 0
    l = [chr(ord('a') + i) for i in range(16)]
    start = l.copy()
    for i in count():
        l = do_dance(inp, l)
        if l == start:
            cyclelen = i + 1
            break
    for i in range(1_000_000_000 % cyclelen):
        l = do_dance(inp, l)
    return ''.join(l)


def parse_maybe(x):
    if x is None:
        return None
    try:
        return int(x)
    except ValueError:
        return x


def solve(inp, ispart1):
    inp = [tuple(map(parse_maybe, re.match(r'^([sxp])(\w|\d+)(?:/(\w|\d+))?$', l).groups())) for l in inp.split(',')]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
