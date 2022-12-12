from aocd import data, submit, AocdError


def solve1(inp):
    return None


def solve2(inp):
    return None


def solve(inp, part1):
    inp = inp.splitlines()
    print(inp)
    if part1:
        return solve1(inp)
    else:
        return solve2(inp)


if __name__ == '__main__':
    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
