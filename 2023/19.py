import re
from functools import reduce
from operator import mul

from aoc_utils import portion_integer as P


def accepted(part, rules, rule="in"):
    if rule == "A":
        return True
    if rule == "R":
        return False
    dim, cmp, value, res1, res2 = rules[rule]
    if (cmp == "<" and part[dim] < value) or (cmp == ">" and part[dim] > value):
        return accepted(part, rules, res1)
    else:
        return accepted(part, rules, res2)


def get_accepted_ranges(rules, rule="in", range=(P.closed(1, 4000),) * 4):
    if rule in "AR":
        if rule == "A":
            yield range
        return
    dim, cmp, value, res1, res2 = rules[rule]
    valid = P.open(-P.inf, value) if cmp == "<" else P.open(value, P.inf)
    range1 = range[:dim] + (range[dim] & valid,) + range[dim + 1:]
    if range1[dim]:
        yield from get_accepted_ranges(rules, res1, range1)
    range2 = range[:dim] + (range[dim] - valid,) + range[dim + 1:]
    if range2[dim]:
        yield from get_accepted_ranges(rules, res2, range2)


def solve(inp, part1):
    workflows, parts = map(str.splitlines, inp.split("\n\n"))
    rules = {}
    for w in workflows:
        rule_name, rest = re.match(r"([a-z]+){([a-z\d:><,RA]+)}", w).groups()
        rests = rest.split(",")
        for i, r in enumerate(rests[:-1]):
            dim, cmp, value, res = re.match(r"([xmas])([<>])(\d+):([a-zRA]+)", r).groups()
            rules[rule_name + ("" if i == 0 else str(i))] = \
                ("xmas".index(dim), cmp, int(value), res, rule_name + str(i + 1))
        dim, cmp, value, res, _ = rules[rule_name + ("" if i == 0 else str(i))]
        rules[rule_name + ("" if i == 0 else str(i))] = (dim, cmp, value, res, rests[-1])

    if part1:
        parts = [tuple(map(int, re.match(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", p).groups())) for p in parts]
        return sum(sum(p) if accepted(p, rules) else 0 for p in parts)
    else:
        return sum(reduce(mul, map(lambda x: x.upper - x.lower + 1, r)) for r in get_accepted_ranges(rules))


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
