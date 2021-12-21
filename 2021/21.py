from collections import Counter
from functools import cache
from itertools import product

from aocd import get_data


def deterministic_die():
    d = 1
    while True:
        yield d
        d = d % 100 + 1


def part1(inp):
    p1pos, p2pos = inp
    p1score, p2score = 0, 0
    die = deterministic_die()
    d = 0
    while True:
        p1pos = (p1pos + sum(next(die) for _ in range(3)) - 1) % 10 + 1
        p1score += p1pos
        d += 3
        if p1score >= 1000:
            break
        p2pos = (p2pos + sum(next(die) for _ in range(3)) - 1) % 10 + 1
        p2score += p2pos
        d += 3
        if p2score >= 1000:
            break
    return min(p1score, p2score) * d


mv_splits = dict(Counter(sum(a) for a in product([1, 2, 3], repeat=3)))


@cache
def calculate_wins(p1pos, p2pos, p1score=0, p2score=0, p1next=True):
    if p1score >= 21:
        return 1, 0
    if p2score >= 21:
        return 0, 1
    p1wins, p2wins = 0, 0
    for move, num in mv_splits.items():
        if p1next:
            np1pos = (p1pos + move - 1) % 10 + 1
            np1score = p1score + np1pos
            np2pos, np2score = p2pos, p2score
        else:
            np2pos = (p2pos + move - 1) % 10 + 1
            np2score = p2score + np2pos
            np1pos, np1score = p1pos, p1score
        w1, w2 = calculate_wins(np1pos, np2pos, np1score, np2score, not p1next)
        p1wins += w1 * num
        p2wins += w2 * num
    return p1wins, p2wins


def part2(inp):
    return max(calculate_wins(*inp))


if __name__ == '__main__':
    data = get_data(day=21, year=2021)
    inp = [int(l.split(' ')[-1]) for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
