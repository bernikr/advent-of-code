from itertools import pairwise


def part1(inp):
    return sum(b > a for a, b in pairwise(inp))


def part2(inp):
    return sum(b > a for a, b in zip(inp, inp[3:]))


def solve(inp, ispart1):
    inp = list(map(int, inp.splitlines()))
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
