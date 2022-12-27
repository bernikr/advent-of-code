import math
from collections import Counter, defaultdict
from itertools import pairwise


def part1(inp):
    current = inp[0]
    for _ in range(10):
        s = ""
        for a, b in pairwise(current):
            s += a + inp[1][a + b]
        current = s + current[-1]
    v = sorted(Counter(current).values())
    return v[-1] - v[0]


def part2(inp):
    pairs = Counter(pairwise(inp[0]))
    for _ in range(40):
        np = defaultdict(lambda: 0)
        for (a, b), c in pairs.items():
            m = inp[1][a + b]
            np[a + m] += c
            np[m + b] += c
        pairs = np
    digits = defaultdict(lambda: 0)
    for (a, b), c in pairs.items():
        digits[a] += c / 2
        digits[b] += c / 2
    v = sorted(math.ceil(d) for d in digits.values())
    return v[-1] - v[0]


def solve(inp, ispart1):
    seq, rules = inp.split('\n\n')
    rules = {a: b for a, b in (l.split(' -> ') for l in rules.splitlines())}
    inp = (seq, rules)
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
