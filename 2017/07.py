import itertools
import re

from aocd import get_data


def part1(a):
    return (set(a.keys())-set(itertools.chain.from_iterable(x[1] for x in a.values()))).pop()


def weight(t, node):
    ws = [weight(t, n) for n in t[node][1]]
    if len(ws) == 0:
        return t[node][0]
    else:
        correct_weight = sorted(ws)[1]
        if min(ws) != max(ws):
            wrong_node = next(n for n in t[node][1] if weight(t, n) != correct_weight)
            print(correct_weight - sum(weight(t, n) for n in t[wrong_node][1]))
        return t[node][0] + len(ws)*correct_weight


def part2(a):
    lowest_node = (set(a.keys())-set(itertools.chain.from_iterable(x[1] for x in a.values()))).pop()
    weight(a, lowest_node)


if __name__ == '__main__':
    data = get_data(day=7, year=2017)
    inp = {l.split(' ')[0]: (int(re.findall(r'\((\d+)\)', l)[0]), l.split(' -> ')[1].split(', ') if '>' in l else [])
           for l in data.splitlines()}
    print(part1(inp))
    part2(inp)
