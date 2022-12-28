import itertools


def part1(a):
    return sum(len(l) == len(set(l)) for l in a)


def part2(a):
    return sum(not any(sorted(a) == sorted(b) for a, b in itertools.combinations(l, 2)) for l in a)


def solve(inp, ispart1):
    inp = [l.split(' ') for l in inp.splitlines()]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
