import itertools
import operator
from collections import defaultdict


def spiral(start=(0, 0)):
    x, y = start
    while True:
        yield (x, y)
        if y <= 0 and y <= x <= -y:
            x += 1
        elif x < 0 and x < y <= -x:
            y -= 1
        elif y > 0 and -y < x <= y:
            x -= 1
        else:
            y += 1


def part1(a):
    return next(sum(map(abs, c)) for i, c in enumerate(spiral()) if i + 1 == a)


def neighbors(c):
    return [tuple(map(operator.add, c, x)) for x in itertools.product([-1, 0, 1], repeat=2) if x[0] != 0 or x[1] != 0]


def added_spiral():
    s = defaultdict(int)
    s[(0, 0)] = 1
    for c in spiral((1, 0)):
        s[c] = sum(s[x] for x in neighbors(c))
        yield s[c]


def part2(a):
    return next(x for x in added_spiral() if x >= a)


def solve(inp, ispart1):
    inp = int(inp)
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
