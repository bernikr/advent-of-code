from functools import cache
from itertools import chain
from operator import itemgetter


def part1(inp):
    return sum(len(d) in [2, 3, 4, 7] for d in chain.from_iterable(map(itemgetter(1), inp)))


@cache
def compute_mapping(digits):
    m = {
        1: next(d for d in digits if len(d) == 2),
        4: next(d for d in digits if len(d) == 4),
        7: next(d for d in digits if len(d) == 3),
        8: next(d for d in digits if len(d) == 7),
    }
    m[9] = next(d for d in digits if len(d) == 6 and m[4].union(m[7]).issubset(d))
    m[6] = next(d for d in digits if len(d) == 6 and len(d.union(m[1])) == 7)
    m[0] = next(d for d in digits if len(d) == 6 and d not in m.values())
    m[5] = next(d for d in digits if len(d) == 5 and d.union(m[6]) == m[6])
    m[3] = next(d for d in digits if len(d) == 5 and d not in m.values() and d.union(m[9]) == m[9])
    m[2] = next(d for d in digits if d not in m.values())
    return {v: k for k, v in m.items()}


def part2(inp):
    return sum(int(''.join(map(str, map(compute_mapping(frozenset(digits)).__getitem__, output))))
               for digits, output in inp)


def solve(inp, ispart1):
    inp = [tuple(map(lambda x: list(map(frozenset, x.split(' '))), l.split(' | '))) for l in inp.splitlines()]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
