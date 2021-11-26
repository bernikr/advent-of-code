from itertools import pairwise, groupby

from aocd import get_data


def part1(a):
    return len([i for i in range(*a) if
                any(a == b for a, b in pairwise(str(i))) and
                all(a <= b for a, b in pairwise(str(i)))])


def part2(a):
    return len([i for i in range(*a) if
                any(len(list(a[1])) == 2 for a in groupby(str(i))) and
                all(a <= b for a, b in pairwise(str(i)))])


if __name__ == '__main__':
    data = get_data(day=4, year=2019)
    inp = tuple(map(int, data.split('-')))
    print(part1(inp))
    print(part2(inp))
