from collections import Counter
from functools import reduce
from operator import itemgetter

from aocd import get_data


def split_by_length(s, l):
    return (s[y-l:y] for y in range(l, len(s)+l, l))


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
    return '\n'.join(''.join('x' if x == '1' else ' ' for x in l) for l in split_by_length(res, 25))


if __name__ == '__main__':
    data = get_data(day=8, year=2019)
    inp = list(split_by_length(data, 25*6))
    print(part1(inp))
    print(part2(inp))
