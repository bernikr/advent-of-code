def part1(a):
    return sum(n for i, n in enumerate(a) if n == a[(i + 1) % len(a)])


def part2(a):
    return sum(n for i, n in enumerate(a) if n == a[(i + len(a) // 2) % len(a)])


def solve(inp, ispart1):
    inp = list(map(int, inp))
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
