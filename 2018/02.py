import itertools
from collections import Counter


def part1(a):
    cs = list(map(Counter, a))
    return sum(2 in c.values() for c in cs) * sum(3 in c.values() for c in cs)


def part2(a):
    return next(''.join(x for x, y in zip(*c) if x == y)
                for c in itertools.combinations(a, 2) if sum(x != y for x, y in zip(*c)) == 1)


def solve(inp, ispart1):
    inp = inp.splitlines()
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
