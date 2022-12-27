def solve1(inp):
    return None


def solve2(inp):
    return None


def solve(inp, part1):
    inp = inp.splitlines()
    print(inp)
    return solve1(inp) if part1 else solve2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
