from itertools import chain
from operator import itemgetter

from aocd import get_data


def part1(inp):
    return sum(len(d) in [2, 3, 4, 7] for d in chain.from_iterable(map(itemgetter(1), inp)))


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
    return {frozenset(v): k for k, v in m.items()}


def part2(inp):
    out = 0
    for all_digits, output in inp:
        m = compute_mapping(all_digits)
        out += int(''.join(map(str, map(m.__getitem__, map(frozenset, output)))))
    return out


if __name__ == '__main__':
    data = get_data(day=8, year=2021)
    inp = [tuple(map(lambda x: list(map(set, x.split(' '))), l.split(' | '))) for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
