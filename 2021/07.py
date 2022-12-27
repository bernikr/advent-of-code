def part1(inp):
    return min(sum(abs(x - c) for x in inp) for c in range(max(inp)))


def part2(inp):
    return min(sum(abs(x - c) * (abs(x - c) + 1) // 2 for x in inp) for c in range(max(inp)))


def solve(inp, ispart1):
    inp = list(map(int, inp.split(',')))
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
