import itertools
import re
from collections import defaultdict
from functools import reduce

from aocd import get_data


def part1(a):
    return sum(x for x in itertools.chain(*a[2]) if
               not any(xmin <= x <= xmax for xmin, xmax in itertools.chain(*a[0].values())))


def part2(a):
    valid_tickets = [t for t in a[2] if
                     all(any(xmin <= x <= xmax for xmin, xmax in itertools.chain(*a[0].values())) for x in t)]
    valid_columns = defaultdict(set)
    for k in a[0].keys():
        for i in range(len(a[2][0])):
            if all(any(xmin <= t[i] <= xmax for xmin, xmax in a[0][k]) for t in valid_tickets):
                valid_columns[k].add(i)
    solved_columns = set()
    key_to_column = {}
    for k, v in sorted(valid_columns.items(), key=lambda x: len(x[1])):
        v = v.difference(solved_columns)
        solved_columns = solved_columns.union(v)
        key_to_column[k] = v.pop()
    return reduce(lambda x, y: x * y, (a[1][v] for k, v in key_to_column.items() if k.startswith('departure')))


if __name__ == '__main__':
    data = get_data(day=16, year=2020)
    input = data.split('\n\n')
    input[0] = {l.split(':')[0]: [(int(x), int(y)) for x, y in re.findall(r'(\d+)-(\d+)', l)] for l in
                input[0].splitlines()}
    input[1] = [int(x) for x in input[1].splitlines()[1].split(',')]
    input[2] = [[int(x) for x in l.split(',')] for l in input[2].splitlines()[1:]]
    print(part1(input))
    print(part2(input))
