from collections import Counter


def part1(a):
    return ''.join(max(Counter(c).items(), key=lambda x: x[1])[0] for c in zip(*a))


def part2(a):
    return ''.join(max(Counter(c).items(), key=lambda x: -x[1])[0] for c in zip(*a))


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
