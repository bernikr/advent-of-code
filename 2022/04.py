def solve1(inp):
    return sum(all(i in range(a, b + 1) for i in range(c, d + 1)) or all(i in range(c, d + 1) for i in range(a, b + 1))
               for (a, b), (c, d) in inp)


def solve2(inp):
    return sum(any(i in range(a, b + 1) for i in range(c, d + 1)) or any(i in range(c, d + 1) for i in range(a, b + 1))
               for (a, b), (c, d) in inp)


def solve(inp, part1):
    inp = [tuple(map(lambda x: tuple(map(int, x.split('-'))), l.split(','))) for l in inp.splitlines()]
    return solve1(inp) if part1 else solve2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
