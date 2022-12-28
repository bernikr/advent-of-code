import re


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


def solve(inp, ispart1):
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
