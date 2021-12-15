import re

from aocd import get_data


def part1(inp):
    out = re.sub(r"!.", "", inp)
    out = re.sub(r"<[^>]*>", "", out)
    lvl = 1
    res = 0
    for c in out:
        if c == '{':
            res += lvl
            lvl += 1
        elif c == '}':
            lvl -= 1
    return res


def part2(inp):
    out = re.sub(r"!.", "", inp)
    out = re.findall(r"<[^>]*>", out)
    return sum(len(a) - 2 for a in out)


if __name__ == '__main__':
    data = get_data(day=9, year=2017)
    inp = data
    print(part1(inp))
    print(part2(inp))
