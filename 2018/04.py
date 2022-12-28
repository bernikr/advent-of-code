import itertools
import operator
import re
from collections import defaultdict
from functools import reduce


def parse_log(log):
    guards = defaultdict(list)
    current_shift, last_asleep = None, None
    for l in log:
        if l[2] is not None:
            if last_asleep is not None:
                for i in range(last_asleep, 60):
                    current_shift[i] = True
            current_shift = [False for _ in range(60)]
            guards[l[2]].append(current_shift)
        elif l[1] == 'falls asleep':
            last_asleep = l[0]
        elif l[1] == 'wakes up':
            for i in range(last_asleep, l[0]):
                current_shift[i] = True
            last_asleep = None
    return guards


def part1(a):
    g = sorted([(g, sum(sum(shift) for shift in shifts)) for g, shifts in a.items()], key=lambda x: -x[1])[0][0]
    m = sorted([(minute, sum(shift[minute] for shift in a[g])) for minute in range(0, 60)], key=lambda x: -x[1])[0][0]
    return g * m


def part2(a):
    return reduce(operator.mul,
                  sorted(
                      [(g, m, sum(shift[m] for shift in a[g])) for g, m in itertools.product(a.keys(), range(0, 60))],
                      key=lambda x: -x[2])[0][:2])


def solve(inp, ispart1):
    inp = parse_log(tuple(map(lambda x: int(x) if x is not None and x.isnumeric() else x,
                              re.match(r'^\[1518-\d+-\d+ \d+:(\d+)] (Guard #(\d+) begins shift|falls asleep|wakes up)',
                                       l).groups()))
                    for l in sorted(inp.splitlines()))
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
