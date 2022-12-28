import itertools
import re
from collections import defaultdict


def get_dependencies(rules):
    dep = defaultdict(list)
    for prev_step, next_step in rules:
        dep[next_step].append(prev_step)
        if prev_step not in dep:
            dep[prev_step] = []
    return dict(dep)


def part1(a):
    dep = get_dependencies(a)
    order = []
    while len(dep) > 0:
        next_step = min(dep.keys(), key=lambda x: (len(dep[x]), x))
        order.append(next_step)
        del dep[next_step]
        for l in dep.values():
            if next_step in l:
                l.remove(next_step)
    return ''.join(order)


def part2(a):
    dep = get_dependencies(a)
    workers = []
    for t in itertools.count():
        for finished, step in workers.copy():
            if finished == t:
                for l in dep.values():
                    if step in l:
                        l.remove(step)
                workers.remove((finished, step))
        while len(workers) < 5 and any(len(l) == 0 for l in dep.values()):
            next_step = min(s for s in dep.keys() if len(dep[s]) == 0)
            del dep[next_step]
            workers.append((t + 60 + ord(next_step) - ord('A') + 1, next_step))
        if len(workers) == 0:
            return t


def solve(inp, ispart1):
    inp = [re.match(r'Step ([A-Z]) must be finished before step ([A-Z]) can begin.', l).groups()
           for l in inp.splitlines()]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
