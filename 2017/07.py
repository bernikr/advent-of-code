import itertools
import re


def part1(a):
    return (set(a.keys()) - set(itertools.chain.from_iterable(x[1] for x in a.values()))).pop()


res = 0
def weight(t, node):
    ws = [weight(t, n) for n in t[node][1]]
    if len(ws) == 0:
        return t[node][0]
    else:
        correct_weight = sorted(ws)[1]
        if min(ws) != max(ws):
            wrong_node = next(n for n in t[node][1] if weight(t, n) != correct_weight)
            global res
            res = (correct_weight - sum(weight(t, n) for n in t[wrong_node][1]))
        return t[node][0] + len(ws) * correct_weight


def part2(a):
    lowest_node = (set(a.keys()) - set(itertools.chain.from_iterable(x[1] for x in a.values()))).pop()
    weight(a, lowest_node)
    global res
    return res


def solve(inp, ispart1):
    inp = {l.split(' ')[0]: (int(re.findall(r'\((\d+)\)', l)[0]), l.split(' -> ')[1].split(', ') if '>' in l else [])
           for l in inp.splitlines()}
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
