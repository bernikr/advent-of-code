import re
from functools import reduce


def all_ratios():
    for a in range(101):
        for b in range(101 - a):
            for c in range(101 - a - b):
                yield (a, b, c, 100 - a - b - c)


def part1(a):
    return max(reduce(lambda x, y: x * y,
                      map(lambda x: (abs(x) + x) // 2,
                          map(sum, zip(*list(map(lambda ingredient, r: [i * r for i in ingredient][:4], a, ratio))))))
               for ratio
               in all_ratios())


def part2(a):
    return max(reduce(lambda x, y: x * y, r[:4]) for r in (list(map(lambda x: (abs(x) + x) // 2, map(sum, zip(
        *list(map(lambda ingredient, r: [i * r for i in ingredient], a, ratio))))))
                                                           for ratio
                                                           in all_ratios()) if r[4] == 500)


def solve(inp, ispart1):
    inp = [tuple(map(int, re.findall(r"-?\d+", l))) for l in inp.splitlines()]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
