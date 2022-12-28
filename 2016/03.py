import itertools
import re


def is_triangle(t):
    t = sorted(t)
    return t[0] + t[1] > t[2]


def part1(a):
    return sum(is_triangle(t) for t in a)


def part2(a):
    return sum(is_triangle(t) for t in (list(itertools.chain(*zip(*a)))[i:i + 3] for i in range(0, len(a) * 3, 3)))


def solve(inp, ispart1):
    inp = [tuple(map(int, re.findall(r"\d+", l))) for l in inp.splitlines()]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
