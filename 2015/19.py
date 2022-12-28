import itertools
import re


def part1(a):
    def custom_replace(s, rule):
        return [s[:match.start()] + rule[1] + s[match.end():] for match in re.finditer(rule[0], s)]

    return len(set(itertools.chain.from_iterable(custom_replace(a[1], rule) for rule in a[0])))


def part2(a):
    # greedy algorithm, could get stuck, but works for the given input
    reverse_rules = sorted([(b, a) for a, b in a[0]], key=lambda x: -len(x[0]))
    mol = a[1]
    c = 0
    while mol != 'e':
        for a, b in reverse_rules:
            if a in mol:
                mol = mol.replace(a, b, 1)
                c += 1
    return c


def solve(inp, ispart1):
    inp = inp.split('\n\n')
    inp[0] = [(l.split(' =>')[0], l.split('=> ')[1]) for l in inp[0].splitlines()]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
