import itertools


def part1(a):
    return sum(max(l) - min(l) for l in a)


def part2(a):
    return sum(next(a // b for a, b in itertools.permutations(l, 2) if a % b == 0) for l in a)


def solve(inp, ispart1):
    inp = [list(map(int, l.split('\t'))) for l in inp.splitlines()]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
