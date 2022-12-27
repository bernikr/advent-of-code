def solve1(inp):
    return max(map(sum, inp))


def solve2(inp):
    return sum(sorted(map(sum, inp))[-3:])


def solve(inp, part1):
    inp = [[int(x) for x in l.splitlines()] for l in inp.split('\n\n')]
    return solve1(inp) if part1 else solve2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
