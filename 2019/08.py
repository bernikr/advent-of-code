from collections import Counter
from functools import reduce
from operator import itemgetter

from aoc_utils import ocr


def split_by_length(s, l):
    return (s[y - l:y] for y in range(l, len(s) + l, l))


def part1(a):
    m = min((Counter(i) for i in a), key=itemgetter('0'))
    return m['1'] * m['2']


def overlay_img(x, y):
    return ''.join(overlay_px(a, b) for a, b in zip(x, y))


def overlay_px(x, y):
    if y == '2':
        return x
    else:
        return y


def part2(a):
    res = reduce(overlay_img, reversed(a))
    return ocr({(x, y) for y, l in enumerate(split_by_length(res, 25)) for x, c in enumerate(l) if c == '1'})


def solve(inp, ispart1):
    inp = list(split_by_length(inp, 25 * 6))
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
