def solve1(inp):
    for i in range(4, len(inp)):
        if len(set(inp[i - 4:i])) == 4:
            return i


def solve2(inp):
    for i in range(14, len(inp)):
        if len(set(inp[i - 14:i])) == 14:
            return i


def solve(inp, part1):
    inp = inp.strip()
    return solve1(inp) if part1 else solve2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
