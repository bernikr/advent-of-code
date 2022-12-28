import itertools
import re
from collections import defaultdict
from functools import reduce


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


def solve(inp, ispart1):
    inp = inp.split('\n\n')
    inp[0] = {l.split(':')[0]: [(int(x), int(y)) for x, y in re.findall(r'(\d+)-(\d+)', l)] for l in
              inp[0].splitlines()}
    inp[1] = [int(x) for x in inp[1].splitlines()[1].split(',')]
    inp[2] = [[int(x) for x in l.split(',')] for l in inp[2].splitlines()[1:]]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
