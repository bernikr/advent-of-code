from itertools import product


def part1(a):
    return next(a * b for a, b in (product((int(l.strip()) for l in a), repeat=2)) if a + b == 2020)


def part2(a):
    return next(a * b * c for a, b, c in (product((int(l.strip()) for l in a), repeat=3)) if a + b + c == 2020)


def solve(inp, ispart1):
    inp = inp.splitlines()
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
