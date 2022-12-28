from functools import reduce


def part1(a):
    return sum(l[i * 3 % len(l)] for i, l in enumerate(a))


def part2(a):
    return reduce(lambda x, y: x * y, (sum(l[i * r % len(l)] for i, l in enumerate(a[::d]))
                                       for r, d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))


def solve(inp, ispart1):
    inp = [[c == '#' for c in l.strip()] for l in inp.splitlines()]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
