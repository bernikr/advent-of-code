def part1(a):
    return max(a)


def part2(a):
    return next(i for i in range(min(a), max(a)) if i not in a and i + 1 in a and i - 1 in a)


def solve(inp, ispart1):
    inp = [int(''.join({"F": "0", "B": "1", "L": "0", "R": "1"}[c] for c in l.strip()), 2) for l in inp.splitlines()]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
