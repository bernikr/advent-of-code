from itertools import chain, combinations

from aocd import get_data


def part1(a):
    return sum(sum(c) == 150 for c in chain.from_iterable(combinations(a, i) for i in range(len(a))))


def part2(a):
    lengths = [len(c) for c in chain.from_iterable(combinations(a, i) for i in range(len(a))) if sum(c) == 150]
    return len([l for l in lengths if l == min(lengths)])


if __name__ == '__main__':
    data = get_data(day=17, year=2015)
    inp = list(map(int, data.splitlines()))
    print(part1(inp))
    print(part2(inp))
